title = "Recepción y validación de instrucciones de embarque"

content = """
- Al recibir un booking del cliente (por correo o portal), verificar que incluya: datos del remitente y consignatario, aeropuerto de origen y destino, tipo de mercancía, peso y volumen estimados, número de bultos, valor declarado, Incoterm, y si aplica, clase de mercancía peligrosa.
- Validar que el destino sea servido por alguna aerolínea con la que AeroCarga tenga contrato. Si no, buscar opciones y cotizar.
- Confirmar al cliente la recepción y asignar un número de referencia interno (REF-XXXX).
- Si la mercancía es peligrosa, solicitar la DGD (Shipper's Declaration for Dangerous Goods) y verificar que la clase esté permitida en la aerolínea y país destino.
- Plazo máximo para confirmar disponibilidad: 2 horas hábiles. Si no hay espacio, informar alternativas.
"""  # noqa: E501

version = "0.0.1"
