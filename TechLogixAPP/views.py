from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Producto, Categoria
from .forms import ProductoForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

# Funciones auxiliares para verificar roles
def es_administrador(user):
    return user.is_superuser or user.groups.filter(name='Administrador').exists()

def es_asistente_o_admin(user):
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name__in=['Administrador', 'Asistente']).exists())

# --- VISTAS PÚBLICAS ---
def index(view_request):
    return render(view_request, 'index.html')

def catalogo(view_request):
    categoria_id = view_request.GET.get('categoria')
    busqueda = view_request.GET.get('q', '')
    
    productos = Producto.objects.all()
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
    if busqueda:
        productos = productos.filter(nombre__icontains=busqueda)
        
    categorias = Categoria.objects.all()
    return render(view_request, 'catalogo.html', {
        'productos': productos,
        'categorias': categorias
    })

# --- SECCIÓN DE ADMINISTRACIÓN (PRIVADA) ---
@login_required(login_url='/admin/login/')
@user_passes_test(es_asistente_o_admin, login_url='/admin/')
def admin_panel(view_request):
    productos = Producto.objects.all()
    es_admin = es_administrador(view_request.user)
    return render(view_request, 'admin_panel.html', {
        'productos': productos,
        'es_admin': es_admin
    })

@login_required(login_url='/admin/login/')
@user_passes_test(es_administrador, login_url='/admin_panel/')
def producto_crear(view_request):
    if view_request.method == 'POST':
        form = ProductoForm(view_request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = ProductoForm()
    return render(view_request, 'producto_form.html', {'form': form, 'accion': 'Crear'})

@login_required(login_url='/admin/login/')
@user_passes_test(es_administrador, login_url='/admin_panel/')
def producto_editar(view_request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if view_request.method == 'POST':
        form = ProductoForm(view_request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = ProductoForm(instance=producto)
    return render(view_request, 'producto_form.html', {'form': form, 'accion': 'Editar'})

@login_required(login_url='/admin/login/')
@user_passes_test(es_administrador, login_url='/admin_panel/')
def producto_eliminar(view_request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if view_request.method == 'POST':
        producto.delete()
        return redirect('admin_panel')
    return render(view_request, 'producto_confirm_delete.html', {'producto': producto})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html' # O tu template de login si usas uno propio, si usas el de admin puedes usar redirección por código abajo:

    def get_success_url(self):
        user = self.request.user
        # Si es superusuario, va al panel nativo de Django (/admin/)
        if user.is_superuser:
            return '/admin/'
        # Cualquier otro usuario (Administrador de grupo o Asistente) va al panel personalizado
        return '/admin_panel/'