# Carta de solicitud de pago – Gráfica Silvestre

Generador web (mismo estilo que actas y proformas) para la **carta de solicitud de pago** a entidades públicas o clientes.

## Uso

```bash
python copiar-logos-desde-acta.py
```

Abra `index.html`, complete el formulario y pulse **Generar PDF**.

## Campos

| Campo | En el PDF |
|-------|-----------|
| Señor / institución | Destinatario |
| Atención | Oficina o área |
| Fecha | Automática (Lima, Perú) |
| N° factura | Asunto y cuerpo |
| Orden de compra | Cuerpo y anexos |
| Concepto | Descripción del servicio |
| Anexos | Lista con viñetas |

## Publicar

Repo nuevo en GitHub Pages con `index.html` y `logos.js`.
