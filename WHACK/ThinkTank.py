import panel as pn
from api import API
import random

# Load JavaScript dependencies for Panel
pn.extension()

FILENAME = "data.csv"

# Initialize API
api = API()
columns_to_load = ["name", "city", "learning_style", "class"]
api.load_data(FILENAME, columns=columns_to_load)

# Widgets for filtering
learning_style_button = pn.widgets.CheckButtonGroup(
    name='learning_style', value=['Visual', 'Auditory', 'Kinesthetic'],
    options=['Visual', 'Auditory', 'Kinesthetic']
)
class_list = pn.widgets.MultiChoice(
    name="class", value=['Data Science', 'Business', 'Finance'],
    options=api.get_classes()
)
city = pn.widgets.MultiSelect(
    name="city", value=['Brookline', 'Boston', 'Newton', 'Quincy', 'Chestnut Hill', 'Roxbury', "Fenway"],
    options=api.get_cities(), size=10
)

# Function to get a random matching student
def get_random_match(learning_style_button, class_list, city):
    # Filter students based on selected criteria
    local = api.extract_local_network(learning_style_button, class_list, city)
    
    if local.empty:
        return "No matching students found."
    
    # Randomly select a student from the filtered list
    matched_student = local.sample(n=1).iloc[0]
    match_info = f"Matched Student: {matched_student['name']} from {matched_student['city']}, " \
                 f"Learning Style: {matched_student['learning_style']}, Class: {matched_student['class']}"
    
    return match_info

# Create a Panel button for finding a random match
random_match_button = pn.widgets.Button(name="Find a Study Buddy", button_type="primary")

# Pane to display the match result
match_result = pn.pane.Markdown("")

# Callback for the button to display a random match
def on_button_click(event):
    match_result.object = get_random_match(
        learning_style_button.value, class_list.value, city.value
    )

# Link the button to the callback
random_match_button.on_click(on_button_click)

# Catalog function for displaying student data in a table
def get_catalog(learning_style_button, class_list, city):
    local = api.extract_local_network(learning_style_button, class_list, city)
    table = pn.widgets.Tabulator(local, selectable=False)
    return table

# Bind the catalog function to the widgets
catalog = pn.bind(get_catalog, learning_style_button, class_list, city)

# Home Page Layout
home_page = pn.Card(
    pn.pane.Markdown("# Welcome to ThinkTank: Study Buddy"),
    pn.pane.Markdown("This is a platform to help you find the best study resources, based on your learning style, classes, and location."),
    pn.pane.Markdown("Use the filters below to explore and visualize the available study spots.")
)

# Search Card Container
card_width = 320
search_card = pn.Card(
    pn.Column(learning_style_button, class_list, city),
    title="Filter", width=card_width, collapsed=False
)

# Layout with matching feature added
layout = pn.template.FastListTemplate(
    title="ThinkTank: Study Buddy",
    sidebar=[home_page, search_card],
    theme_toggle=False,
    main=[
        pn.Tabs(
            ("Students", catalog),
            ("Good Match", pn.Column(random_match_button, match_result)),
            active=0
        )
    ],
    header_background='#f79295'
).servable()

layout.show()