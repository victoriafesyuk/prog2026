import gradio as gr
import re


def detect_labels(text: str, regexp: str, mark_as: str) -> list[dict]:
    entities = []

    for match in re.finditer(regexp, text):
        entities.append(
            {
                "entity": mark_as,
                "start": match.start(),
                "end": match.end(),
            }
        )     
    return entities     

def detect_numbers(text: str) -> dict:
    
    return {
        "text": text, 
        "entities": (
            detect_labels(text, r"\b(я|мене|мені|мною|ти|тебе|тобі|тобою|він|його|йому|ним|вона|її|нею|воно|його|йому|ним|ми|нас|нам|нами|ви|вас|вам|вами|вони|їх|їм|ними)\b", "особові займеннки")
            + detect_labels(text, r"\b[А-ЩЬЮЯЄІЇҐ][а-щьюяєіїґ]+\b", "capital letter")
            + detect_labels(text, r"\b[А-Яа-яґҐєЄіІїЇ]*([бвгґджзйклмнпрстфхцчшщБВГҐДЖЗЙКЛМНПРСТФХЦЧШЩ])\1[А-Яа-яґҐєЄіІїЇ]*\b", "подвоєння")
        ),
    }

app = gr.Interface(
    fn=detect_numbers,
    inputs=gr.Text(label="Введіть текст", placeholder="Текст..."),
    outputs=gr.HighlightedText(
        label="Відповідь", color_map={"особові займенники": "green", "capital letter": "blue", "подвоєння": "purple" }
    ),
    flagging_mode="never"
)

app.launch()