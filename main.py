from shiny import App, reactive, render, ui
import asyncio

import height_weight

app_ui = ui.page_fluid(
    ui.tags.style("""
        .centered-column {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .centered-column > * {
            margin-bottom: 10px;
        }
        .centered-text {
            max-width: 600px;
            width: 100%;
            text-align: center;
        }
    """),
    ui.tags.div(
        {"class": "centered-column"},
        ui.tags.div(
            {"class": "centered-text"},
            ui.output_text("hello")
        ),
        ui.input_action_button("action_button1", "Рост и вес подростков"),
        ui.output_ui("progress"),
        ui.output_plot("height_weight_plot"),
    )
)

def server(input, output, session):
    @output
    @render.text
    def hello():
        return "Здравствуйте! В этом приложении вы можете построить парную линейную регрессию для предустановленного датафрейма с данными о росте и весе американских подростков"

    @output
    @render.plot
    @reactive.event(input.action_button1)
    def height_weight_plot():
        return height_weight.plot()

    @output
    @render.ui
    @reactive.event(input.action_button1)
    async def progress():
        with ui.Progress(min=1, max=25) as p:
            p.set(message="Calculation in progress", detail="This may take a while...")

            for i in range(1, 25):
                p.set(i, message="Computing")
                await asyncio.sleep(0.1)

        return

app = App(app_ui, server)
app.run()