# app/models/__init__.py
# Importar todos los modelos para que Base los registre
from .alertassistema import AlertaSistema
from .categoria import Categoria
from .clientes import Cliente
from .compras import Compra
from .comprobante import Comprobante
from .configuracionglobal import ConfiguracionGlobal
from .dashboard import Dashboard
from .detallecompras import DetalleCompra
from .detalleventas import DetalleVenta
from .empresa import Empresa
from .filtrosreportes import FiltroReporte
from .integracionesapi import IntegracionAPI
from .inventario import Inventario
from .inventariosucursal import InventarioSucursal
from .kpi import KPI
from .logia import LogIA
from .notificaciones import Notificacion
from .parametrossistema import ParametroSistema
from .plantillascomprobante import PlantillaComprobante
from .productos import Producto
from .proveedores import Proveedor
from .reportes import Reporte
from .roles import Rol
from .rubrossistema import RubroSistema
from .sucursal import Sucursal
from .sugerenciascompra import SugerenciaCompra
from .usuarios import Usuario
from .ventas import Venta
# Si quieres mantener orden, sigue agregando imports conforme creamos archivos
