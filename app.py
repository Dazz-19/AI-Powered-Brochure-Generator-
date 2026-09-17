
from brochure import create_brochure
import gradio as gr

with gr.Blocks(title="Brochure Generator", theme="gradio/soft") as demo:
    gr.Markdown("# 📄 Brochure in a Jiffy")

    website = gr.Textbox(
        label="🌐 Website URL",
        placeholder="https://www.anthropic.com",
        lines=1
    )

    submit = gr.Button("🚀 Generate Brochure", variant="primary", size="lg")

    output = gr.HTML(label="Generated Brochure")

    with gr.Row():
        html_download = gr.File(label="Download html")
        pdf_download = gr.File(label="Download pdf")

    word_limit = gr.Slider(
        minimum=50,
        maximum=200,
        value=100,
        step=15,
        label="📝 Number of words"
    )

    submit.click(
        fn=create_brochure,
        inputs=[website, word_limit],
        outputs=[output, html_download, pdf_download]
    )

    gr.Examples(
        examples=[
            ["https://www.anthropic.com"],
            ["https://gradio.app"],
            ["https://huggingface.co"]
        ],
        inputs=website
    )

demo.launch()