#
# THIS FILE IS GENERATED; DO NOT EDIT
#

from typing import Optional, Union, List
from .cards import Value, PackedRecord, PackedRecords, PackedData
from .cards import \
    BasicList, \
    Button, \
    Buttons, \
    Card1, \
    Card2, \
    Card3, \
    Card4, \
    Card5, \
    Card6, \
    Card7, \
    Card8, \
    Card9, \
    Cell, \
    Checkbox, \
    Checklist, \
    Choice, \
    ChoiceGroup, \
    ColorPicker, \
    Combobox, \
    Command, \
    Component, \
    Dashboard, \
    DashboardPage, \
    DashboardPanel, \
    DashboardRow, \
    DataCell, \
    DataSource, \
    DatePicker, \
    Dropdown, \
    Expander, \
    FileUpload, \
    Flex, \
    Form, \
    FrameCell, \
    Grid, \
    HeadingCell, \
    Label, \
    Link, \
    ListItem1, \
    Mark, \
    Markdown, \
    MarkdownCell, \
    Markup, \
    MessageBar, \
    Nav, \
    NavGroup, \
    NavItem, \
    Notebook, \
    NotebookSection, \
    PixelArt, \
    Plot, \
    Progress, \
    Query, \
    Repeat, \
    Separator, \
    Slider, \
    Spinbox, \
    Tab, \
    Table, \
    TableColumn, \
    TableRow, \
    Tabs, \
    Template, \
    Text, \
    Textbox, \
    Toggle, \
    VegaCell, \
    Vis


def basic_list(
        box: str,
        title: str,
        item_view: str,
        item_props: PackedRecord,
        data: PackedData,
) -> BasicList:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param item_view: No documentation available.
    :param item_props: No documentation available.
    :param data: No documentation available.
    """
    return BasicList(
        box,
        title,
        item_view,
        item_props,
        data,
    )


def card1(
        box: str,
        title: str,
        value: str,
        data: Optional[PackedRecord] = None,
) -> Card1:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param data: No documentation available.
    """
    return Card1(
        box,
        title,
        value,
        data,
    )


def card2(
        box: str,
        title: str,
        value: str,
        aux_value: str,
        data: PackedRecord,
        plot_type: str,
        plot_data: PackedData,
        plot_color: str,
        plot_category: str,
        plot_value: str,
        plot_zero_value: float,
        plot_curve: str,
) -> Card2:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param data: No documentation available.
    :param plot_type: No documentation available. One of 'area', 'interval'.
    :param plot_data: No documentation available.
    :param plot_color: No documentation available.
    :param plot_category: No documentation available.
    :param plot_value: No documentation available.
    :param plot_zero_value: No documentation available.
    :param plot_curve: No documentation available.
    """
    return Card2(
        box,
        title,
        value,
        aux_value,
        data,
        plot_type,
        plot_data,
        plot_color,
        plot_category,
        plot_value,
        plot_zero_value,
        plot_curve,
    )


def card3(
        box: str,
        title: str,
        value: str,
        aux_value: str,
        caption: str,
        data: PackedRecord,
) -> Card3:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param caption: No documentation available.
    :param data: No documentation available.
    """
    return Card3(
        box,
        title,
        value,
        aux_value,
        caption,
        data,
    )


def card4(
        box: str,
        title: str,
        value: str,
        aux_value: str,
        progress: float,
        plot_color: str,
        data: PackedRecord,
) -> Card4:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param progress: No documentation available.
    :param plot_color: No documentation available.
    :param data: No documentation available.
    """
    return Card4(
        box,
        title,
        value,
        aux_value,
        progress,
        plot_color,
        data,
    )


def card5(
        box: str,
        title: str,
        value: str,
        aux_value: str,
        progress: float,
        plot_color: str,
        data: PackedRecord,
) -> Card5:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param progress: No documentation available.
    :param plot_color: No documentation available.
    :param data: No documentation available.
    """
    return Card5(
        box,
        title,
        value,
        aux_value,
        progress,
        plot_color,
        data,
    )


def card6(
        box: str,
        title: str,
        value: str,
        aux_value: str,
        data: PackedRecord,
        plot_type: str,
        plot_data: PackedData,
        plot_color: str,
        plot_category: str,
        plot_value: str,
        plot_zero_value: float,
        plot_curve: str,
) -> Card6:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param data: No documentation available.
    :param plot_type: No documentation available. One of 'area', 'interval'.
    :param plot_data: No documentation available.
    :param plot_color: No documentation available.
    :param plot_category: No documentation available.
    :param plot_value: No documentation available.
    :param plot_zero_value: No documentation available.
    :param plot_curve: No documentation available.
    """
    return Card6(
        box,
        title,
        value,
        aux_value,
        data,
        plot_type,
        plot_data,
        plot_color,
        plot_category,
        plot_value,
        plot_zero_value,
        plot_curve,
    )


def card7(
        box: str,
        title: str,
        value: str,
        data: PackedRecord,
        plot_type: str,
        plot_data: PackedData,
        plot_color: str,
        plot_category: str,
        plot_value: str,
        plot_zero_value: float,
        plot_curve: str,
) -> Card7:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param data: No documentation available.
    :param plot_type: No documentation available. One of 'area', 'interval'.
    :param plot_data: No documentation available.
    :param plot_color: No documentation available.
    :param plot_category: No documentation available.
    :param plot_value: No documentation available.
    :param plot_zero_value: No documentation available.
    :param plot_curve: No documentation available.
    """
    return Card7(
        box,
        title,
        value,
        data,
        plot_type,
        plot_data,
        plot_color,
        plot_category,
        plot_value,
        plot_zero_value,
        plot_curve,
    )


def card8(
        box: str,
        title: str,
        value: str,
        aux_value: str,
        progress: float,
        plot_color: str,
        data: PackedRecord,
) -> Card8:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param progress: No documentation available.
    :param plot_color: No documentation available.
    :param data: No documentation available.
    """
    return Card8(
        box,
        title,
        value,
        aux_value,
        progress,
        plot_color,
        data,
    )


def card9(
        box: str,
        title: str,
        caption: str,
        value: str,
        aux_value: str,
        value_caption: str,
        aux_value_caption: str,
        progress: float,
        plot_color: str,
        data: PackedRecord,
) -> Card9:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param caption: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param value_caption: No documentation available.
    :param aux_value_caption: No documentation available.
    :param progress: No documentation available.
    :param plot_color: No documentation available.
    :param data: No documentation available.
    """
    return Card9(
        box,
        title,
        caption,
        value,
        aux_value,
        value_caption,
        aux_value_caption,
        progress,
        plot_color,
        data,
    )


def heading_cell(
        level: int,
        content: str,
) -> Cell:
    """No documentation available.

    :param level: No documentation available.
    :param content: No documentation available.
    """
    return Cell(heading=HeadingCell(
        level,
        content,
    ))


def markdown_cell(
        content: str,
) -> Cell:
    """No documentation available.

    :param content: No documentation available.
    """
    return Cell(markdown=MarkdownCell(
        content,
    ))


def frame_cell(
        source: str,
        width: str,
        height: str,
) -> Cell:
    """No documentation available.

    :param source: No documentation available.
    :param width: No documentation available.
    :param height: No documentation available.
    """
    return Cell(frame=FrameCell(
        source,
        width,
        height,
    ))


def data_cell(
        content: str,
) -> Cell:
    """No documentation available.

    :param content: No documentation available.
    """
    return Cell(data=DataCell(
        content,
    ))


def data_source(
        t: str,
        id: int,
) -> DataSource:
    """No documentation available.

    :param t: No documentation available. One of 'Table', 'View'.
    :param id: No documentation available.
    """
    return DataSource(
        t,
        id,
    )


def query(
        sql: str,
        sources: List[DataSource],
) -> Query:
    """No documentation available.

    :param sql: No documentation available.
    :param sources: No documentation available.
    """
    return Query(
        sql,
        sources,
    )


def vega_cell(
        specification: str,
        query: Query,
) -> Cell:
    """No documentation available.

    :param specification: No documentation available.
    :param query: No documentation available.
    """
    return Cell(vega=VegaCell(
        specification,
        query,
    ))


def cell(
        heading: Optional[HeadingCell] = None,
        markdown: Optional[MarkdownCell] = None,
        frame: Optional[FrameCell] = None,
        data: Optional[DataCell] = None,
        vega: Optional[VegaCell] = None,
) -> Cell:
    """No documentation available.

    :param heading: No documentation available.
    :param markdown: No documentation available.
    :param frame: No documentation available.
    :param data: No documentation available.
    :param vega: No documentation available.
    """
    return Cell(
        heading,
        markdown,
        frame,
        data,
        vega,
    )


def command(
        action: str,
        icon: str,
        label: str,
        caption: str,
        data: str,
) -> Command:
    """No documentation available.

    :param action: No documentation available.
    :param icon: No documentation available.
    :param label: No documentation available.
    :param caption: No documentation available.
    :param data: No documentation available.
    """
    return Command(
        action,
        icon,
        label,
        caption,
        data,
    )


def dashboard_panel(
        cells: List[Cell],
        size: str,
        commands: List[Command],
        data: str,
) -> DashboardPanel:
    """No documentation available.

    :param cells: No documentation available.
    :param size: No documentation available.
    :param commands: No documentation available.
    :param data: No documentation available.
    """
    return DashboardPanel(
        cells,
        size,
        commands,
        data,
    )


def dashboard_row(
        panels: List[DashboardPanel],
        size: str,
) -> DashboardRow:
    """No documentation available.

    :param panels: No documentation available.
    :param size: No documentation available.
    """
    return DashboardRow(
        panels,
        size,
    )


def dashboard_page(
        title: str,
        rows: List[DashboardRow],
) -> DashboardPage:
    """No documentation available.

    :param title: No documentation available.
    :param rows: No documentation available.
    """
    return DashboardPage(
        title,
        rows,
    )


def dashboard(
        box: str,
        pages: List[DashboardPage],
) -> Dashboard:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param pages: No documentation available.
    """
    return Dashboard(
        box,
        pages,
    )


def flex(
        box: str,
        title: str,
        item_view: str,
        item_props: PackedRecord,
        direction: str,
        justify: str,
        align: str,
        wrap: str,
        data: PackedData,
) -> Flex:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param item_view: No documentation available.
    :param item_props: No documentation available.
    :param direction: No documentation available. One of 'horizontal', 'vertical'.
    :param justify: No documentation available. One of 'start', 'end', 'center', 'between', 'around'.
    :param align: No documentation available. One of 'start', 'end', 'center', 'baseline', 'stretch'.
    :param wrap: No documentation available. One of 'start', 'end', 'center', 'between', 'around', 'stretch'.
    :param data: No documentation available.
    """
    return Flex(
        box,
        title,
        item_view,
        item_props,
        direction,
        justify,
        align,
        wrap,
        data,
    )


def text(
        content: str,
        size: Optional[str] = None,
        tooltip: Optional[str] = None,
) -> Component:
    """Create text content.

    :param content: The text content.
    :param size: The font size of the text content. One of "xl" (extra large), "l" (large), "m" (medium), "s" (small), "xs" (extra small).
    :param tooltip: An optional tooltip message displayed when a user clicks the help icon to the right of the component.
    """
    return Component(text=Text(
        content,
        size,
        tooltip,
    ))


def label(
        label: str,
        required: Optional[bool] = None,
        disabled: Optional[bool] = None,
        tooltip: Optional[str] = None,
) -> Component:
    """Create a label.

    Labels give a name or title to a component or group of components.
    Labels should be in close proximity to the component or group they are paired with.
    Some components, such as textboxes, dropdowns, or toggles, already have labels
    incorporated, but other components may optionally add a Label if it helps inform
    the user of the component’s purpose.

    :param label: The text displayed on the label.
    :param required: True if the field is required.
    :param disabled: True if the label should be disabled.
    :param tooltip: An optional tooltip message displayed when a user clicks the help icon to the right of the component.
    """
    return Component(label=Label(
        label,
        required,
        disabled,
        tooltip,
    ))


def separator(
        label: Optional[str] = None,
) -> Component:
    """Create a separator.

    A separator visually separates content into groups.

    :param label: The text displayed on the separator.
    """
    return Component(separator=Separator(
        label,
    ))


def progress(
        label: str,
        caption: Optional[str] = None,
        value: Optional[float] = None,
        tooltip: Optional[str] = None,
) -> Component:
    """Create a progress bar.

    Progress bars are used to show the completion status of an operation lasting more than 2 seconds.
    If the state of progress cannot be determined, do not set a value.
    Progress bars feature a bar showing total units to completion, and total units finished.
    The label appears above the bar, and the caption appears below.
    The label should tell someone exactly what the operation is doing.

    Examples of formatting include:
    [Object] is being [operation name], or
    [Object] is being [operation name] to [destination name] or
    [Object] is being [operation name] from [source name] to [destination name]

    Status text is generally in units elapsed and total units.
    Real-world examples include copying files to a storage location, saving edits to a file, and more.
    Use units that are informative and relevant to give the best idea to users of how long the operation will take to complete.
    Avoid time units as they are rarely accurate enough to be trustworthy.
    Also, combine steps of a complex operation into one total bar to avoid “rewinding” the bar.
    Instead change the label to reflect the change if necessary. Bars moving backwards reduce confidence in the service.

    :param label: The text displayed above the bar.
    :param caption: The text displayed below the bar.
    :param value: The progress, between 0.0 and 1.0, or -1 (default) if indeterminate.
    :param tooltip: An optional tooltip message displayed when a user clicks the help icon to the right of the component.
    """
    return Component(progress=Progress(
        label,
        caption,
        value,
        tooltip,
    ))


def message_bar(
        type: Optional[str] = None,
        text: Optional[str] = None,
) -> Component:
    """Create a message bar.

    A message bar is an area at the top of a primary view that displays relevant status information.
    You can use a message bar to tell the user about a situation that does not require their immediate attention and
    therefore does not need to block other activities.

    :param type: The icon and color of the message bar. One of 'info', 'error', 'warning', 'success', 'danger', 'blocked'.
    :param text: The text displayed on the message bar.
    """
    return Component(message_bar=MessageBar(
        type,
        text,
    ))


def textbox(
        name: str,
        label: Optional[str] = None,
        value: Optional[str] = None,
        placeholder: Optional[str] = None,
        mask: Optional[str] = None,
        icon: Optional[str] = None,
        prefix: Optional[str] = None,
        suffix: Optional[str] = None,
        error: Optional[str] = None,
        required: Optional[bool] = None,
        disabled: Optional[bool] = None,
        readonly: Optional[bool] = None,
        multiline: Optional[bool] = None,
        password: Optional[bool] = None,
        tooltip: Optional[str] = None,
) -> Component:
    """Create a text box.

    The text box component enables a user to type text into an app.
    It's typically used to capture a single line of text, but can be configured to capture multiple lines of text.
    The text displays on the screen in a simple, uniform format.

    :param name: An identifying name for this component.
    :param label: The text displayed above the field.
    :param value: Text to be displayed inside the text box.
    :param placeholder: A string that provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that demonstrates the expected type of data, rather than an explanatory message.
    :param mask: The masking string that defines the mask's behavior. A backslash will escape any character. Special format characters are: '9': [0-9] 'a': [a-zA-Z] '*': [a-zA-Z0-9].
    :param icon: Icon displayed in the far right end of the text field.
    :param prefix: Text to be displayed before the text box contents.
    :param suffix: Text to be displayed after the text box contents.
    :param error: Text to be displayed as an error below the text box.
    :param required: True if the text box is a required field.
    :param disabled: True if the text box is disabled.
    :param readonly: True if the text box is a read-only field.
    :param multiline: True if the text box should allow multi-line text entry.
    :param password: True if the text box should hide text content.
    :param tooltip: An optional tooltip message displayed when a user clicks the help icon to the right of the component.
    """
    return Component(textbox=Textbox(
        name,
        label,
        value,
        placeholder,
        mask,
        icon,
        prefix,
        suffix,
        error,
        required,
        disabled,
        readonly,
        multiline,
        password,
        tooltip,
    ))


def checkbox(
        name: str,
        label: str,
        value: bool,
        indeterminate: bool,
        disabled: bool,
        trigger: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param value: No documentation available.
    :param indeterminate: No documentation available.
    :param disabled: No documentation available.
    :param trigger: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(checkbox=Checkbox(
        name,
        label,
        value,
        indeterminate,
        disabled,
        trigger,
        tooltip,
    ))


def toggle(
        name: str,
        label: str,
        value: bool,
        disabled: bool,
        trigger: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param value: No documentation available.
    :param disabled: No documentation available.
    :param trigger: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(toggle=Toggle(
        name,
        label,
        value,
        disabled,
        trigger,
        tooltip,
    ))


def choice(
        name: str,
        label: str,
        disabled: bool,
) -> Choice:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param disabled: No documentation available.
    """
    return Choice(
        name,
        label,
        disabled,
    )


def choice_group(
        name: str,
        label: str,
        value: str,
        choices: List[Choice],
        required: bool,
        trigger: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param value: No documentation available.
    :param choices: No documentation available.
    :param required: No documentation available.
    :param trigger: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(choice_group=ChoiceGroup(
        name,
        label,
        value,
        choices,
        required,
        trigger,
        tooltip,
    ))


def checklist(
        name: str,
        label: str,
        values: List[str],
        choices: List[Choice],
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param values: No documentation available.
    :param choices: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(checklist=Checklist(
        name,
        label,
        values,
        choices,
        tooltip,
    ))


def dropdown(
        name: str,
        label: str,
        placeholder: str,
        multiple: bool,
        value: str,
        values: List[str],
        choices: List[Choice],
        required: bool,
        disabled: bool,
        trigger: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param placeholder: No documentation available.
    :param multiple: No documentation available.
    :param value: No documentation available.
    :param values: No documentation available.
    :param choices: No documentation available.
    :param required: No documentation available.
    :param disabled: No documentation available.
    :param trigger: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(dropdown=Dropdown(
        name,
        label,
        placeholder,
        multiple,
        value,
        values,
        choices,
        required,
        disabled,
        trigger,
        tooltip,
    ))


def combobox(
        name: str,
        label: str,
        placeholder: str,
        value: str,
        choices: List[str],
        error: str,
        disabled: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param placeholder: No documentation available.
    :param value: No documentation available.
    :param choices: No documentation available.
    :param error: No documentation available.
    :param disabled: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(combobox=Combobox(
        name,
        label,
        placeholder,
        value,
        choices,
        error,
        disabled,
        tooltip,
    ))


def slider(
        name: str,
        label: str,
        min: float,
        max: float,
        step: float,
        value: float,
        disabled: bool,
        trigger: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param min: No documentation available.
    :param max: No documentation available.
    :param step: No documentation available.
    :param value: No documentation available.
    :param disabled: No documentation available.
    :param trigger: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(slider=Slider(
        name,
        label,
        min,
        max,
        step,
        value,
        disabled,
        trigger,
        tooltip,
    ))


def spinbox(
        name: str,
        label: str,
        min: float,
        max: float,
        step: float,
        value: float,
        disabled: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param min: No documentation available.
    :param max: No documentation available.
    :param step: No documentation available.
    :param value: No documentation available.
    :param disabled: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(spinbox=Spinbox(
        name,
        label,
        min,
        max,
        step,
        value,
        disabled,
        tooltip,
    ))


def date_picker(
        name: str,
        label: str,
        placeholder: str,
        value: str,
        disabled: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param placeholder: No documentation available.
    :param value: No documentation available.
    :param disabled: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(date_picker=DatePicker(
        name,
        label,
        placeholder,
        value,
        disabled,
        tooltip,
    ))


def color_picker(
        name: str,
        label: str,
        value: str,
        choices: List[str],
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param value: No documentation available.
    :param choices: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(color_picker=ColorPicker(
        name,
        label,
        value,
        choices,
        tooltip,
    ))


def button(
        name: str,
        label: str,
        caption: str,
        primary: bool,
        disabled: bool,
        link: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param caption: No documentation available.
    :param primary: No documentation available.
    :param disabled: No documentation available.
    :param link: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(button=Button(
        name,
        label,
        caption,
        primary,
        disabled,
        link,
        tooltip,
    ))


def buttons(
        buttons: List[Button],
) -> Component:
    """No documentation available.

    :param buttons: No documentation available.
    """
    return Component(buttons=Buttons(
        buttons,
    ))


def file_upload(
        name: str,
        label: str,
        multiple: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param multiple: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(file_upload=FileUpload(
        name,
        label,
        multiple,
        tooltip,
    ))


def table_column(
        name: str,
        label: str,
) -> TableColumn:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    """
    return TableColumn(
        name,
        label,
    )


def table_row(
        name: str,
        cells: List[str],
) -> TableRow:
    """No documentation available.

    :param name: No documentation available.
    :param cells: No documentation available.
    """
    return TableRow(
        name,
        cells,
    )


def table(
        name: str,
        columns: List[TableColumn],
        rows: List[TableRow],
        multiple: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param columns: No documentation available.
    :param rows: No documentation available.
    :param multiple: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(table=Table(
        name,
        columns,
        rows,
        multiple,
        tooltip,
    ))


def link(
        label: str,
        path: str,
        disabled: bool,
        button: bool,
        tooltip: str,
) -> Component:
    """No documentation available.

    :param label: No documentation available.
    :param path: No documentation available.
    :param disabled: No documentation available.
    :param button: No documentation available.
    :param tooltip: No documentation available.
    """
    return Component(link=Link(
        label,
        path,
        disabled,
        button,
        tooltip,
    ))


def tab(
        name: str,
        label: str,
        icon: str,
) -> Tab:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param icon: No documentation available.
    """
    return Tab(
        name,
        label,
        icon,
    )


def tabs(
        name: str,
        value: str,
        items: List[Tab],
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param value: No documentation available.
    :param items: No documentation available.
    """
    return Component(tabs=Tabs(
        name,
        value,
        items,
    ))


def expander(
        name: str,
        label: str,
        expanded: bool,
        items: List[Component],
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    :param expanded: No documentation available.
    :param items: No documentation available.
    """
    return Component(expander=Expander(
        name,
        label,
        expanded,
        items,
    ))


def nav_item(
        name: str,
        label: str,
) -> NavItem:
    """No documentation available.

    :param name: No documentation available.
    :param label: No documentation available.
    """
    return NavItem(
        name,
        label,
    )


def nav_group(
        label: str,
        items: List[NavItem],
) -> NavGroup:
    """No documentation available.

    :param label: No documentation available.
    :param items: No documentation available.
    """
    return NavGroup(
        label,
        items,
    )


def nav(
        name: str,
        items: List[NavGroup],
) -> Component:
    """No documentation available.

    :param name: No documentation available.
    :param items: No documentation available.
    """
    return Component(nav=Nav(
        name,
        items,
    ))


def component(
        text: Optional[Text] = None,
        label: Optional[Label] = None,
        separator: Optional[Separator] = None,
        progress: Optional[Progress] = None,
        message_bar: Optional[MessageBar] = None,
        textbox: Optional[Textbox] = None,
        checkbox: Optional[Checkbox] = None,
        toggle: Optional[Toggle] = None,
        choice_group: Optional[ChoiceGroup] = None,
        checklist: Optional[Checklist] = None,
        dropdown: Optional[Dropdown] = None,
        combobox: Optional[Combobox] = None,
        slider: Optional[Slider] = None,
        spinbox: Optional[Spinbox] = None,
        date_picker: Optional[DatePicker] = None,
        color_picker: Optional[ColorPicker] = None,
        buttons: Optional[Buttons] = None,
        file_upload: Optional[FileUpload] = None,
        table: Optional[Table] = None,
        link: Optional[Link] = None,
        tabs: Optional[Tabs] = None,
        button: Optional[Button] = None,
        expander: Optional[Expander] = None,
        nav: Optional[Nav] = None,
) -> Component:
    """No documentation available.

    :param text: No documentation available.
    :param label: No documentation available.
    :param separator: No documentation available.
    :param progress: No documentation available.
    :param message_bar: No documentation available.
    :param textbox: No documentation available.
    :param checkbox: No documentation available.
    :param toggle: No documentation available.
    :param choice_group: No documentation available.
    :param checklist: No documentation available.
    :param dropdown: No documentation available.
    :param combobox: No documentation available.
    :param slider: No documentation available.
    :param spinbox: No documentation available.
    :param date_picker: No documentation available.
    :param color_picker: No documentation available.
    :param buttons: No documentation available.
    :param file_upload: No documentation available.
    :param table: No documentation available.
    :param link: No documentation available.
    :param tabs: No documentation available.
    :param button: No documentation available.
    :param expander: No documentation available.
    :param nav: No documentation available.
    """
    return Component(
        text,
        label,
        separator,
        progress,
        message_bar,
        textbox,
        checkbox,
        toggle,
        choice_group,
        checklist,
        dropdown,
        combobox,
        slider,
        spinbox,
        date_picker,
        color_picker,
        buttons,
        file_upload,
        table,
        link,
        tabs,
        button,
        expander,
        nav,
    )


def form(
        box: str,
        url: str,
        args: PackedRecord,
        items: Union[List[Component], str],
) -> Form:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param url: No documentation available.
    :param args: No documentation available.
    :param items: No documentation available.
    """
    return Form(
        box,
        url,
        args,
        items,
    )


def grid(
        box: str,
        title: str,
        cells: PackedData,
        data: PackedData,
) -> Grid:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param cells: No documentation available.
    :param data: No documentation available.
    """
    return Grid(
        box,
        title,
        cells,
        data,
    )


def list_item1(
        box: str,
        title: str,
        caption: str,
        value: str,
        aux_value: str,
        data: PackedRecord,
) -> ListItem1:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param caption: No documentation available.
    :param value: No documentation available.
    :param aux_value: No documentation available.
    :param data: No documentation available.
    """
    return ListItem1(
        box,
        title,
        caption,
        value,
        aux_value,
        data,
    )


def markdown(
        box: str,
        title: str,
        content: str,
        data: Optional[PackedRecord] = None,
) -> Markdown:
    """Render Markdown content.

    :param box: A string indicating how to place this component on the page.
    :param title: The title for this card.
    :param content: The markdown content. Supports Github Flavored Markdown (GFM): https://guides.github.com/features/mastering-markdown/
    :param data: Additional data for the card.
    """
    return Markdown(
        box,
        title,
        content,
        data,
    )


def markup(
        box: str,
        title: str,
        content: str,
) -> Markup:
    """Render HTML content.

    :param box: A string indicating how to place this component on the page.
    :param title: The title for this card.
    :param content: The HTML content.
    """
    return Markup(
        box,
        title,
        content,
    )


def notebook_section(
        cells: List[Cell],
        commands: List[Command],
        data: str,
) -> NotebookSection:
    """No documentation available.

    :param cells: No documentation available.
    :param commands: No documentation available.
    :param data: No documentation available.
    """
    return NotebookSection(
        cells,
        commands,
        data,
    )


def notebook(
        box: str,
        sections: List[NotebookSection],
) -> Notebook:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param sections: No documentation available.
    """
    return Notebook(
        box,
        sections,
    )


def pixel_art(
        box: str,
        title: str,
        data: PackedRecord,
) -> PixelArt:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param data: No documentation available.
    """
    return PixelArt(
        box,
        title,
        data,
    )


def mark(
        coord: Optional[str] = None,
        mark: Optional[str] = None,
        x: Optional[Value] = None,
        x0: Optional[Value] = None,
        x1: Optional[Value] = None,
        x2: Optional[Value] = None,
        x_min: Optional[float] = None,
        x_max: Optional[float] = None,
        x_nice: Optional[bool] = None,
        x_scale: Optional[str] = None,
        x_title: Optional[str] = None,
        y: Optional[Value] = None,
        y0: Optional[Value] = None,
        y1: Optional[Value] = None,
        y2: Optional[Value] = None,
        y_min: Optional[float] = None,
        y_max: Optional[float] = None,
        y_nice: Optional[bool] = None,
        y_scale: Optional[str] = None,
        y_title: Optional[str] = None,
        color: Optional[str] = None,
        color_range: Optional[str] = None,
        shape: Optional[str] = None,
        shape_range: Optional[str] = None,
        size: Optional[float] = None,
        size_range: Optional[str] = None,
        stack: Optional[str] = None,
        dodge: Optional[str] = None,
        curve: Optional[str] = None,
        fill_color: Optional[str] = None,
        fill_opacity: Optional[float] = None,
        stroke_color: Optional[str] = None,
        stroke_opacity: Optional[float] = None,
        stroke_size: Optional[float] = None,
        stroke_dash: Optional[str] = None,
        label: Optional[str] = None,
        label_offset: Optional[float] = None,
        label_offset_x: Optional[float] = None,
        label_offset_y: Optional[float] = None,
        label_rotation: Optional[str] = None,
        label_position: Optional[str] = None,
        label_overlap: Optional[str] = None,
        label_fill_color: Optional[str] = None,
        label_fill_opacity: Optional[float] = None,
        label_stroke_color: Optional[str] = None,
        label_stroke_opacity: Optional[float] = None,
        label_stroke_size: Optional[float] = None,
        label_font_size: Optional[float] = None,
        label_font_weight: Optional[str] = None,
        label_line_height: Optional[float] = None,
        label_align: Optional[str] = None,
        ref_stroke_color: Optional[str] = None,
        ref_stroke_opacity: Optional[float] = None,
        ref_stroke_size: Optional[float] = None,
        ref_stroke_dash: Optional[str] = None,
) -> Mark:
    """No documentation available.

    :param coord: No documentation available.
    :param mark: No documentation available.
    :param x: No documentation available.
    :param x0: No documentation available.
    :param x1: No documentation available.
    :param x2: No documentation available.
    :param x_min: No documentation available.
    :param x_max: No documentation available.
    :param x_nice: No documentation available.
    :param x_scale: No documentation available.
    :param x_title: No documentation available.
    :param y: No documentation available.
    :param y0: No documentation available.
    :param y1: No documentation available.
    :param y2: No documentation available.
    :param y_min: No documentation available.
    :param y_max: No documentation available.
    :param y_nice: No documentation available.
    :param y_scale: No documentation available.
    :param y_title: No documentation available.
    :param color: No documentation available.
    :param color_range: No documentation available.
    :param shape: No documentation available.
    :param shape_range: No documentation available.
    :param size: No documentation available.
    :param size_range: No documentation available.
    :param stack: No documentation available.
    :param dodge: No documentation available.
    :param curve: No documentation available. One of 'none', 'smooth', 'step-before', 'step', 'step-after'.
    :param fill_color: No documentation available.
    :param fill_opacity: No documentation available.
    :param stroke_color: No documentation available.
    :param stroke_opacity: No documentation available.
    :param stroke_size: No documentation available.
    :param stroke_dash: No documentation available.
    :param label: No documentation available.
    :param label_offset: No documentation available.
    :param label_offset_x: No documentation available.
    :param label_offset_y: No documentation available.
    :param label_rotation: No documentation available.
    :param label_position: No documentation available.
    :param label_overlap: No documentation available.
    :param label_fill_color: No documentation available.
    :param label_fill_opacity: No documentation available.
    :param label_stroke_color: No documentation available.
    :param label_stroke_opacity: No documentation available.
    :param label_stroke_size: No documentation available.
    :param label_font_size: No documentation available.
    :param label_font_weight: No documentation available.
    :param label_line_height: No documentation available.
    :param label_align: No documentation available.
    :param ref_stroke_color: No documentation available.
    :param ref_stroke_opacity: No documentation available.
    :param ref_stroke_size: No documentation available.
    :param ref_stroke_dash: No documentation available.
    """
    return Mark(
        coord,
        mark,
        x,
        x0,
        x1,
        x2,
        x_min,
        x_max,
        x_nice,
        x_scale,
        x_title,
        y,
        y0,
        y1,
        y2,
        y_min,
        y_max,
        y_nice,
        y_scale,
        y_title,
        color,
        color_range,
        shape,
        shape_range,
        size,
        size_range,
        stack,
        dodge,
        curve,
        fill_color,
        fill_opacity,
        stroke_color,
        stroke_opacity,
        stroke_size,
        stroke_dash,
        label,
        label_offset,
        label_offset_x,
        label_offset_y,
        label_rotation,
        label_position,
        label_overlap,
        label_fill_color,
        label_fill_opacity,
        label_stroke_color,
        label_stroke_opacity,
        label_stroke_size,
        label_font_size,
        label_font_weight,
        label_line_height,
        label_align,
        ref_stroke_color,
        ref_stroke_opacity,
        ref_stroke_size,
        ref_stroke_dash,
    )


def vis(
        marks: List[Mark],
) -> Vis:
    """No documentation available.

    :param marks: No documentation available.
    """
    return Vis(
        marks,
    )


def plot(
        box: str,
        title: str,
        data: PackedRecord,
        vis: Vis,
) -> Plot:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param data: No documentation available.
    :param vis: No documentation available.
    """
    return Plot(
        box,
        title,
        data,
        vis,
    )


def repeat(
        box: str,
        title: str,
        item_view: str,
        item_props: PackedRecord,
        data: PackedData,
) -> Repeat:
    """No documentation available.

    :param box: A string indicating how to place this component on the page.
    :param title: No documentation available.
    :param item_view: No documentation available.
    :param item_props: No documentation available.
    :param data: No documentation available.
    """
    return Repeat(
        box,
        title,
        item_view,
        item_props,
        data,
    )


def template(
        box: str,
        title: str,
        content: str,
        data: Optional[PackedRecord] = None,
) -> Template:
    """Render dynamic content using a HTML template.

    :param box: A string indicating how to place this component on the page.
    :param title: The title for this card.
    :param content: The Handlebars template. https://handlebarsjs.com/guide/
    :param data: Data for the Handlebars template
    """
    return Template(
        box,
        title,
        content,
        data,
    )
