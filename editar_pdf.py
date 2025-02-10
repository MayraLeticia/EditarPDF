import fitz  

# Abrir o PDF
doc = fitz.open("novembro.pdf")

# Mapeamento de datas para substituição (Maio → Agosto)
date_mapping = {
    "01/05/2025": "01/11/2025",
    "02/05/2025": "02/11/2025",
    "03/05/2025": "03/11/2025",
    "04/05/2025": "04/11/2025",
    "05/05/2025": "05/11/2025",
    "06/05/2025": "06/11/2025",
    "07/05/2025": "07/11/2025",
    "08/05/2025": "08/11/2025",
    "09/05/2025": "09/11/2025",
    "10/05/2025": "10/11/2025",
    "11/05/2025": "11/11/2025",
    "12/05/2025": "12/11/2025",
    "13/05/2025": "13/11/2025",
    "14/05/2025": "14/11/2025",
    "15/05/2025": "15/11/2025",
    "16/05/2025": "16/11/2025",
    "17/05/2025": "17/11/2025",
    "18/05/2025": "18/11/2025",
    "19/05/2025": "19/11/2025",
    "20/05/2025": "20/11/2025",
    "21/05/2025": "21/11/2025",
    "22/05/2025": "22/11/2025",
    "23/05/2025": "23/11/2025",
    "24/05/2025": "24/11/2025",
    "25/05/2025": "25/11/2025",
    "26/05/2025": "26/11/2025",
    "27/05/2025": "27/11/2025",
    "28/05/2025": "28/11/2025",
    "29/05/2025": "29/11/2025",
    "30/05/2025": "30/11/2025",
    "31/05/2025": "31/11/2025"
}

# Mapeamento de dias da semana conforme o novo mês
week_mapping = {
    "5ª Feira": "Sábado",
    "6ª Feira": "Domingo",
    "Sábado": "2ª Feira",
    "Domingo": "3ª Feira",
    "2ª Feira": "4ª Feira",
    "3ª Feira": "5ª Feira",
    "4ª Feira": "6ª Feira"
}

# Percorre cada página
for page_num, page in enumerate(doc):
    for texto_antigo, texto_novo in date_mapping.items():
        text_instances = page.search_for(texto_antigo)  # Procura pelo texto na página

        if text_instances:  # Se o texto for encontrado
            print(f"Data encontrada na página {page_num + 1}, substituindo...")

            for inst in text_instances:
                rect = fitz.Rect(inst)  # Obtém a posição do texto
                
                # Cobre a área do texto antigo com um retângulo branco
                page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1), overlay=True)

                # Insere o novo texto na mesma posição
                page.insert_text(
                    (rect.x0 + 4, rect.y0 + 7.5),
                    texto_novo,
                    fontsize=9, 
                    color=(0, 0, 0),
                    overlay=True
                )

    for texto_antigo, texto_novo in week_mapping.items():
        text_instances = page.search_for(texto_antigo)  # Procura pelo texto na página

        if text_instances:  # Se o texto for encontrado
            print(f"Dia da semana encontrado na página {page_num + 1}, substituindo...")

            for inst in text_instances:
                rect = fitz.Rect(inst)  # Obtém a posição do texto
                
                # Cobre a área do texto antigo com um retângulo branco
                page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1), overlay=True)

                # Insere o novo texto na mesma posição
                page.insert_text(
                    (rect.x0 + 4, rect.y0 + 7.5),
                    texto_novo,
                    fontsize=9, 
                    color=(0, 0, 0),
                    overlay=True
                )
            break  # Substitui apenas a primeira ocorrência por página

# Salvar o novo PDF
doc.save("novembro_editado.pdf")
doc.close()

print("Novo PDF salvo como 'novembro_editado.pdf'")
