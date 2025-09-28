# Required imports
from spotpear import *
import random
import math
import machine
import st77xx
import lvgl as lv


timer1 = machine.Timer(-1)
timer2 = machine.Timer(-1)
timer3 = machine.Timer(-1)
timer4 = machine.Timer(-1)
timer5 = machine.Timer(-1)

#encoded_data = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACAAQAAAADrRVxmAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAACYktHRAAAqo0jMgAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+kJHA8MFFdztvAAAALcSURBVEjHjdYxyuM4FAfwv/CsvUWIi21UBDRHiDulseYoA75AwK3BWtJ+TC5g8FXkxu6SKwjM4NYmjQzBb3GW2d357G/WKn+SQE960hPoXYMG7wJzRNrnTyHBllASB9WhCd8OB0gaNkDhcTspox79oXXSRGsgqKn6/TksLHdbAZL1wC6xYhuUxMkFJuxTLTr390p/hjlaWUe39C3h3Y/wfw1EjmrJ7n1ScDdv4QKeHhdGMoM/ii/fEbMXuBlE0XarcLlYQMbqQgUJo2gJ2gMg/UgDXgBW4ekF3Klm6AGv89dAC0dmQpw+rMDYvAO3Ch4XmI7xbpcDsWRLKKnrmjpm/TmxzlXVBigEAjkOtyy0wir6ALj7D9iEyDjWn9OCXFCtgM5gaZzUW3ixfFLNBmjnw5FQl6ttyYdagk5g3ckcd7vEccmGDWAzyydm9ued1wYyoCUUueCM7n2WaAsZR/9C+iEcumB0rHpcypaqSW2Ai0XnWGWAjHcAW4L1nCWzDx8Pap1qmvdwX44oWy5UNdzO8Ozr3i5AJ86xOrrPM+aeDWAB+P4R3lWjgx9uACISp2ZSOi9F5ytagTbgMcL79UFwvgw2QUesuinSoqVqbH4GM84Jw101mjhDDutUtQGK3Dmf3Y6eFqBXar+HP9uA+2D48in7nbuaoX1BZM67jHNXqxXQnZhPMstLyyG3wDPhwKnfI3wegFO1hLLsRDNOIT2eAr4aNoA9CBer4ZY+PQtZRyvwWQDxEZ7+bPFbHaFtCYhjdtFfWxFMagWeooN/jLNQ2wAm2gBWODuOw7csbEVAk/oBt39A56B6LgVhAYv53v4vELmA1XHY5xceqIaWoCHcqaq+pf3BkpzfoF/A1xeUJCzU/fq4ag+qWYG5NEJVBp6es569wKnBIC3shxCMYx/1Wd6Kmg3bQMg46tNr6dkpZksoSTiJ/TEl3QYmGDaAhoCP/T6l0oIcW8L778ZfhnrowbaPR8kAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjUtMDktMjhUMTU6MTI6MTQrMDA6MDBDx3pyAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDI1LTA5LTI4VDE1OjEyOjE0KzAwOjAwMprCzgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyNS0wOS0yOFQxNToxMjoyMCswMDowMB9PwOEAAAAhdEVYdGhpc3RvZ3JhbTpjb250cmFzdC1zdHJldGNoADB4MTAwJXXjKWEAAAAASUVORK5CYII="
import ubinascii
encoded_data = "iVBORw0KGgoAAAANSUhEUgAAAIAAAACAAQAAAADrRVxmAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAACYktHRAAAqo0jMgAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+kJHA8MFFdztvAAAALcSURBVEjHjdYxyuM4FAfwv/CsvUWIi21UBDRHiDulseYoA75AwK3BWtJ+TC5g8FXkxu6SKwjM4NYmjQzBb3GW2d357G/WKn+SQE960hPoXYMG7wJzRNrnTyHBllASB9WhCd8OB0gaNkDhcTspox79oXXSRGsgqKn6/TksLHdbAZL1wC6xYhuUxMkFJuxTLTr390p/hjlaWUe39C3h3Y/wfw1EjmrJ7n1ScDdv4QKeHhdGMoM/ii/fEbMXuBlE0XarcLlYQMbqQgUJo2gJ2gMg/UgDXgBW4ekF3Klm6AGv89dAC0dmQpw+rMDYvAO3Ch4XmI7xbpcDsWRLKKnrmjpm/TmxzlXVBigEAjkOtyy0wir6ALj7D9iEyDjWn9OCXFCtgM5gaZzUW3ixfFLNBmjnw5FQl6ttyYdagk5g3ckcd7vEccmGDWAzyydm9ued1wYyoCUUueCM7n2WaAsZR/9C+iEcumB0rHpcypaqSW2Ai0XnWGWAjHcAW4L1nCWzDx8Pap1qmvdwX44oWy5UNdzO8Ozr3i5AJ86xOrrPM+aeDWAB+P4R3lWjgx9uACISp2ZSOi9F5ytagTbgMcL79UFwvgw2QUesuinSoqVqbH4GM84Jw101mjhDDutUtQGK3Dmf3Y6eFqBXar+HP9uA+2D48in7nbuaoX1BZM67jHNXqxXQnZhPMstLyyG3wDPhwKnfI3wegFO1hLLsRDNOIT2eAr4aNoA9CBer4ZY+PQtZRyvwWQDxEZ7+bPFbHaFtCYhjdtFfWxFMagWeooN/jLNQ2wAm2gBWODuOw7csbEVAk/oBt39A56B6LgVhAYv53v4vELmA1XHY5xceqIaWoCHcqaq+pf3BkpzfoF/A1xeUJCzU/fq4ag+qWYG5NEJVBp6es569wKnBIC3shxCMYx/1Wd6Kmg3bQMg46tNr6dkpZksoSTiJ/TEl3QYmGDaAhoCP/T6l0oIcW8L778ZfhnrowbaPR8kAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjUtMDktMjhUMTU6MTI6MTQrMDA6MDBDx3pyAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDI1LTA5LTI4VDE1OjEyOjE0KzAwOjAwMprCzgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyNS0wOS0yOFQxNToxMjoyMCswMDowMB9PwOEAAAAhdEVYdGhpc3RvZ3JhbTpjb250cmFzdC1zdHJldGNoADB4MTAwJXXjKWEAAAAASUVORK5CYII="
raw_image = ubinascii.a2b_base64(encoded_data)
encoded_data = None  # Free memory
# Create image descriptor
image_dsc = lv.image_dsc_t()
image_dsc.data = raw_image
image_dsc.data_size = len(raw_image)

# Display the image
img = lv.image(lv.screen_active())
img.set_src(image_dsc)
img.center()


import ubinascii
encoded_data = "iVBORw0KGgoAAAANSUhEUgAAAIAAAACAAQAAAADrRVxmAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAACYktHRAAAqo0jMgAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+kJHA8MFFdztvAAAALcSURBVEjHjdYxyuM4FAfwv/CsvUWIi21UBDRHiDulseYoA75AwK3BWtJ+TC5g8FXkxu6SKwjM4NYmjQzBb3GW2d357G/WKn+SQE960hPoXYMG7wJzRNrnTyHBllASB9WhCd8OB0gaNkDhcTspox79oXXSRGsgqKn6/TksLHdbAZL1wC6xYhuUxMkFJuxTLTr390p/hjlaWUe39C3h3Y/wfw1EjmrJ7n1ScDdv4QKeHhdGMoM/ii/fEbMXuBlE0XarcLlYQMbqQgUJo2gJ2gMg/UgDXgBW4ekF3Klm6AGv89dAC0dmQpw+rMDYvAO3Ch4XmI7xbpcDsWRLKKnrmjpm/TmxzlXVBigEAjkOtyy0wir6ALj7D9iEyDjWn9OCXFCtgM5gaZzUW3ixfFLNBmjnw5FQl6ttyYdagk5g3ckcd7vEccmGDWAzyydm9ued1wYyoCUUueCM7n2WaAsZR/9C+iEcumB0rHpcypaqSW2Ai0XnWGWAjHcAW4L1nCWzDx8Pap1qmvdwX44oWy5UNdzO8Ozr3i5AJ86xOrrPM+aeDWAB+P4R3lWjgx9uACISp2ZSOi9F5ytagTbgMcL79UFwvgw2QUesuinSoqVqbH4GM84Jw101mjhDDutUtQGK3Dmf3Y6eFqBXar+HP9uA+2D48in7nbuaoX1BZM67jHNXqxXQnZhPMstLyyG3wDPhwKnfI3wegFO1hLLsRDNOIT2eAr4aNoA9CBer4ZY+PQtZRyvwWQDxEZ7+bPFbHaFtCYhjdtFfWxFMagWeooN/jLNQ2wAm2gBWODuOw7csbEVAk/oBt39A56B6LgVhAYv53v4vELmA1XHY5xceqIaWoCHcqaq+pf3BkpzfoF/A1xeUJCzU/fq4ag+qWYG5NEJVBp6es569wKnBIC3shxCMYx/1Wd6Kmg3bQMg46tNr6dkpZksoSTiJ/TEl3QYmGDaAhoCP/T6l0oIcW8L778ZfhnrowbaPR8kAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjUtMDktMjhUMTU6MTI6MTQrMDA6MDBDx3pyAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDI1LTA5LTI4VDE1OjEyOjE0KzAwOjAwMprCzgAAACh0RVh0ZGF0ZTp0aW1lc3RhbXAAMjAyNS0wOS0yOFQxNToxMjoyMCswMDowMB9PwOEAAAAhdEVYdGhpc3RvZ3JhbTpjb250cmFzdC1zdHJldGNoADB4MTAwJXXjKWEAAAAASUVORK5CYII="
raw_image = ubinascii.a2b_base64(encoded_data)

img_dsc = lv.image_dsc_t({'data_size': len(raw_image), 'data': memoryview(raw_image)})
img = lv.image(lv.screen_active())
img.set_src(img_dsc)






def init_display():
    spi = machine.SPI( 1, baudrate=40_000_000, polarity=0, phase=0, sck=machine.Pin(3, machine.Pin.OUT), mosi=machine.Pin(4, machine.Pin.OUT), )
    disp = st77xx.St7735(rot=st77xx.ST77XX_INV_LANDSCAPE,res=(128,128), model='redtab', spi=spi, cs=2, dc=0, rst=5, rp2_dma=None, )
    scr = lv.obj()
    lv.screen_load(scr)
    clear_screen(0xffffff)

def rbg_to_rgb( hexcolor ):
    """Convert 0xRBG to 0xRGB color format."""
    r = (hexcolor & 0xFF0000) >> 16
    b = (hexcolor & 0x00FF00) >> 8
    g = (hexcolor & 0x0000FF)
    return (r << 16) | (g << 8) | b


def clear_screen( color=0x003a57 ):
    screen = lv.screen_active()
    screen.clean()
    set_screen_background( color )

def set_screen_background( color ) :
    screen = lv.screen_active()
    screen.set_style_bg_color(lv.color_hex(rbg_to_rgb(color)), lv.PART.MAIN)


# Define the callback function to be called after 5 seconds
def on_timer_trigger_timer1(timer):
    print("Timer 1 expired! Calling the next function...")


# Expects gloabal timers 1..5
def set_timer( timer, _period = 5000 ):
    # Create a one-shot timer that triggers after 5000 milliseconds (5 seconds)
    if timer == 1:
        timer1.init(mode=machine.Timer.ONE_SHOT, period=_period, callback=on_timer_trigger_timer1)
    elif timer == 2:
        timer2.init(mode=machine.Timer.ONE_SHOT, period=_period, callback=on_timer_trigger_timer2)
    elif timer == 3:
        timer3.init(mode=machine.Timer.ONE_SHOT, period=_period, callback=on_timer_trigger_timer3)
    elif timer == 4:
        timer4.init(mode=machine.Timer.ONE_SHOT, period=_period, callback=on_timer_trigger_timer4)
    elif timer == 5:
        timer5.init(mode=machine.Timer.ONE_SHOT, period=_period, callback=on_timer_trigger_timer5)


def draw_pixel( x=0, y=0, _color=0xff0000 ):
    scr = lv.screen_active()
    pixel = lv.obj(scr)
    pixel.set_size(10, 10)
    pixel.set_pos(x, y)
    pixel.set_style_bg_color(lv.color_hex(_color), 0)
    return pixel

def draw_rectangle(x=10, y=10, width=20, height=20, _color=0x00ff00):
    scr = lv.screen_active()
    color = lv.color_hex(rbg_to_rgb(_color))
    rect = lv.obj(scr)
    rect.set_size(width, height)
    rect.set_pos(x, y)
    rect.set_style_bg_color(color, 0)
    rect.remove_flag(lv.obj.FLAG.SCROLLABLE)
    rect.set_style_radius(0,lv.PART.MAIN)
    return rect


def draw_line(x1=10, y1=10, x2=50, y2=50, _color=0x0000ff, width=2):
    scr = lv.screen_active()
    color = lv.color_hex(rbg_to_rgb(_color))
    line = lv.line(scr)
    line.set_points([lv.point_precise_t({"x": x1, "y": y1}), lv.point_precise_t({"x": x2, "y": y2})],2)
    line.set_style_line_color(color, 0)
    line.set_style_line_width(width, 0)
    return line


def draw_circle(x=10, y=10, radius=10, _color=0xff0000):
    scr = lv.screen_active()
    color = lv.color_hex(rbg_to_rgb(_color))
    circle = lv.obj(scr)
    circle.set_size(radius * 2, radius * 2)
    circle.set_pos(x - radius, y - radius)
    circle.set_style_bg_color(color, 0)
    circle.set_style_radius(lv.RADIUS_CIRCLE, 0)
    return circle



def display_text_at_position(label_text="Hello World!", x=10, y=10, color=0xffffff, size=14):
    screen = lv.screen_active()
    label = lv.label(screen)
    lv.label.set_text(label, label_text)
    label.set_pos(x, y)
    label_style = lv.style_t()
    label_style.init()
    if size == 14:
        font = lv.font_montserrat_14
    elif size == 16:
        font = lv.font_montserrat_16
    elif size == 24:
        font = lv.font_montserrat_24
    else:
        font = lv.font_montserrat_14  # Default to 14 if size is unrecognized
    label_style.set_text_font(font)
    label_style.set_text_color(lv.color_hex(rbg_to_rgb(color)))
    label.add_style(label_style, 0)
    return label


def display_text_marquee_in_container(label_text="Hello World!", x=10, y=10, color=0xffffff, size=14):
    screen = lv.screen_active()
    container = lv.obj(screen)
    container.set_size(100, 30)  # Set container size
    container.set_pos(x, y)
    container.set_style_clip_corner(True, 0)  # Enable clipping
    container.set_style_bg_color(lv.color_hex(0x000000), 0)  # Optional: set background color
    container.remove_flag(lv.obj.FLAG.SCROLLABLE)  # Disable scrolling
    # Create the label inside the container
    label = lv.label(container)
    lv.label.set_text(label, label_text)
    label.set_pos(0, 5)  # Initial position inside the container
    # Apply style to the label
    label_style = lv.style_t()
    label_style.init()
    if size == 14:
        font = lv.font_montserrat_14
    elif size == 16:
        font = lv.font_montserrat_16
    elif size == 24:
        font = lv.font_montserrat_24
    else:
        font = lv.font_montserrat_14  # Default to 14 if size is unrecognized
    label_style.set_text_font(font)
    label_style.set_text_color(lv.color_hex(rbg_to_rgb(color)))
    label.add_style(label_style, 0)
    # Calculate text width and set up animation if needed
    label.refresh_ext_draw_size()  # Ensure the label's size is updated
    text_width = label.get_width()
    container_width = container.get_width()
    # Only animate if text is wider than container
    if text_width > container_width:
        anim = lv.anim_t()
        anim.init()
        anim.set_var(label)
        anim.set_values(0, -(text_width))
        anim.set_time(5000 + (len(label_text) * 100))  # Duration based on text length
        anim.set_repeat_count(lv.ANIM_REPEAT_INFINITE)
        anim.set_path_cb(lv.anim_path_linear)
        anim.start()
    
    return container


def parse_matrix(input_str):
    """
    Converts a colon-separated string of digits into an NxN matrix of integers.
    
    Example:
        '09090:90909:90009:09090:00900' → 
        [[0,9,0,9,0],
         [9,0,9,0,9],
         [9,0,0,0,9],
         [0,9,0,9,0],
         [0,0,9,0,0]]
    """
    rows = input_str.split(':')
    matrix = [[int(char) for char in row] for row in rows]
    
    # Optional: Validate it's a square matrix
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise ValueError("Input does not form a square NxN matrix.")
    
    return matrix


def draw_grid(grid, border, square_color, screen_width, screen_height):
    N = len(grid)
    if N == 0 or any(len(row) != N for row in grid):
        raise ValueError("Grid must be NxN")
    # Calculate available space and square size
    total_border_x = border * (N + 1)
    total_border_y = border * (N + 1)
    square_width = (screen_width - total_border_x) // N
    square_height = (screen_height - total_border_y) // N
    # Get the current screen
    screen = lv.screen_active()
    # Draw each square
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 1:
                x = border + col * (square_width + border)
                y = border + row * (square_height + border)
                #
                square = lv.obj(screen)
                square.set_size(square_width, square_height)
                square.set_pos(x, y)
                square.remove_flag(lv.obj.FLAG.SCROLLABLE)
                square.set_style_radius(0,lv.PART.MAIN)
                #
                square.set_style_bg_color(lv.color_hex(rbg_to_rgb(square_color)), lv.PART.MAIN)
                # We just dont draw anything if its missing
                #else:
                #    square.set_style_bg_color(lv.color_hex(0xFFFFFF), lv.PART.MAIN)
                #
                square.set_style_border_width(1, lv.PART.MAIN)
                square.set_style_border_color(lv.color_hex(0x000000), lv.PART.MAIN)



def set_pin( boolean ):
    from machine import Pin
    led = Pin(11, Pin.OUT)
    if boolean == 0:
        led.off()
    else:
        led.on()

def get_button( button_number ):
    from machine import Pin
    button1 = Pin(8, Pin.IN, Pin.PULL_UP)
    button2 = Pin(10, Pin.IN, Pin.PULL_UP)
    if button_number == 1:
        return button1.value()
    elif button_number == 2:
        return button2.value()
    else:
        return None




###########################################################
#
# Various test code for the above
#

example_array = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
]
BACKGROUND_COLOR = 0x2C3E50  # Dark blue-gray
SQUARE_COLOR = 0x3498DB      # Light blue
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 128
BORDER_SIZE = 5

init_display()


import lvgl as lv

init_display()
draw_grid(example_array, border=5, square_color=0xFF00FF, screen_width=128, screen_height=128)





>>> print(dir(lv))
['__class__', '__init__', '__name__', 'list', 'map', 'pow', 'ALIGN', 'ANIM_IMAGE_PART', 'ANIM_PLAYTIME_INFINITE', 'ANIM_REPEAT_INFINITE', 
 'BASE_DIR', 'BLEND_MODE', 'BORDER_SIDE', 'BUTTONMATRIX_BUTTON_NONE', 'CACHE_RESERVE_COND', 'CHART_POINT_NONE', 'COLOR_DEPTH', 'COLOR_FORMAT',
   'COORD', 'COVER_RES', 'C_Pointer', 'DIR', 'DISPLAY_RENDER_MODE', 'DISPLAY_ROTATION', 'DPI_DEF', 'DRAW_BUF_ALIGN', 'DRAW_BUF_STRIDE_ALIGN', 'DRAW_SW_MASK_LINE_SIDE', 'DRAW_SW_MASK_RES', 'DRAW_SW_MASK_TYPE', 'DRAW_TASK_STATE', 'DRAW_TASK_TYPE', 'DROPDOWN_POS_LAST', 'EVENT', 'FLEX_ALIGN', 'FLEX_FLOW', 'FONT_FMT_TXT', 'FONT_FMT_TXT_CMAP', 'FONT_GLYPH_FORMAT', 'FONT_KERNING', 'FONT_SUBPX', 'FS_MODE', 'FS_RES', 'FS_SEEK', 'GRAD_DIR', 'GRAD_EXTEND',
  'GRID_ALIGN', 'GRID_CONTENT', 'GRID_TEMPLATE_LAST', 'GROUP_REFOCUS_POLICY', 'IMAGE_HEADER_MAGIC', 'INDEV_GESTURE', 'INDEV_MODE', 'INDEV_STATE', 'INDEV_TYPE', 'KEY', 'LABEL_DOT_NUM', 'LABEL_POS_LAST', 'LABEL_TEXT_SELECTION_OFF', 'LAYER_TYPE', 'LAYOUT', 'LOG_LEVEL', 'LvReferenceError', 'OPA', 'PALETTE', 'PART', 'PART_TEXTAREA', 'RADIUS_CIRCLE', 'RB_COLOR', 'RESULT', 'SCALE_LABEL_ENABLED_DEFAULT', 'SCALE_LABEL_ROTATE_KEEP_UPRIGHT', 'SCALE_LABEL_ROTATE_MATCH_TICKS', 'SCALE_MAJOR_TICK_EVERY_DEFAULT', 'SCALE_NONE', 'SCALE_ROTATION_ANGLE_MASK', 'SCALE_TOTAL_TICK_COUNT_DEFAULT', 
  'SCROLLBAR_MODE', 'SCROLL_SNAP', 'SCR_LOAD_ANIM', 'SIZE_CONTENT', 'SPAN_MODE', 'SPAN_OVERFLOW', 'STATE', 'STRIDE_AUTO', 'STR_SYMBOL', 
  'STYLE', 'STYLE_RES', 'STYLE_STATE_CMP', 'SUBJECT_TYPE', 'SYMBOL', 'TABLE_CELL_NONE', 'TEXTAREA_CURSOR_LAST', 'TEXT_ALIGN', 
  'TEXT_CMD_STATE', 'TEXT_DECOR', 'TEXT_FLAG', 'THREAD_PRIO', 'TREE_WALK', '__del__', '__dict__', '_lv_mp_int_wrapper', '_nesting', 
  'anim_bezier3_para_t', 'anim_core_deinit', 'anim_core_init', 'anim_count_running', 'anim_delete', 'anim_delete_all', 'anim_get', 
  'anim_get_timer', 'anim_parameter_t', 'anim_refr_now', 'anim_resolve_speed', 'anim_speed', 'anim_speed_clamped', 'anim_speed_to_time', 
  'anim_state_t', 'anim_t', 'anim_timeline_create', 'anim_timeline_t', 'animimg', 'animimg_class', 'arc', 'arc_class', 'area_t', 'array_t',
    'async_call', 'async_call_cancel', 'atan2', 'bar', 'bar_class', 'barcode', 'barcode_class', 'bezier3', 'bidi_calculate_align', 
    'bin_decoder_close', 'bin_decoder_get_area', 'bin_decoder_info', 'bin_decoder_init', 'bin_decoder_open', 'binfont_create', 
    'binfont_create_from_buffer', 'binfont_destroy', 'binfont_font_class', 'builtin_font_class', 'button', 'button_class', 'buttonmatrix', 'buttonmatrix_class', 'cache_class_lru_ll_count', 'cache_class_lru_ll_size', 'cache_class_lru_rb_count', 'cache_class_lru_rb_size', 'cache_class_t', 'cache_entry_alloc', 'cache_entry_get_entry', 'cache_entry_get_size', 'cache_entry_t', 'cache_ops_t', 'cache_slot_size_t', 'cache_t', 'calendar', 'calendar_class', 'calendar_date_t', 'calendar_header_arrow_class', 'calendar_header_dropdown_class', 'calloc', 'canvas', 'canvas_class', 'chart', 'chart_class', 'chart_cursor_t', 'chart_series_t', 'checkbox', 'checkbox_class', 'circle_buf_create', 'circle_buf_create_from_array', 'circle_buf_create_from_buf', 'circle_buf_t', 'clamp_height', 'clamp_width', 'color16_t', 'color24_luminance', 'color32_make', 'color32_t', 'color_16_16_mix', 'color_black', 'color_filter_dsc_t', 'color_filter_shade', 'color_format_get_bpp', 'color_format_get_size', 'color_format_has_alpha', 'color_hex', 'color_hex3', 'color_hsv_t', 'color_hsv_to_rgb', 'color_make', 'color_rgb_to_hsv', 'color_swap_16', 'color_t', 'color_white', 'cubic_bezier', 'deinit', 'delay_ms', 'delay_set_cb', 'display_create', 'display_get_default', 'display_refr_timer', 'display_t', 'dpx', 'draw_add_task', 'draw_arc', 'draw_arc_dsc_t', 'draw_arc_get_area', 'draw_border', 'draw_border_dsc_t', 'draw_box_shadow', 'draw_box_shadow_dsc_t', 'draw_buf_align', 'draw_buf_create', 'draw_buf_get_font_handlers', 'draw_buf_get_handlers', 'draw_buf_get_image_handlers', 'draw_buf_handlers_t', 'draw_buf_init_handlers', 'draw_buf_t', 'draw_buf_width_to_stride', 'draw_character', 'draw_create_unit', 'draw_deinit', 'draw_dispatch', 'draw_dispatch_request', 'draw_dispatch_wait_for_request', 'draw_dsc_base_t', 'draw_fill', 'draw_fill_dsc_t', 'draw_finalize_task_creation', 'draw_get_available_task', 'draw_get_next_available_task', 'draw_get_unit_count', 'draw_global_info_t', 'draw_glyph_dsc_t', 'draw_image', 'draw_image_dsc_t', 'draw_image_sup_t', 'draw_init', 'draw_label', 'draw_label_dsc_t', 'draw_label_hint_t', 'draw_layer', 'draw_layer_alloc_buf', 'draw_layer_create', 'draw_layer_go_to_xy', 'draw_layer_init', 'draw_letter', 'draw_letter_dsc_t', 'draw_line', 'draw_line_dsc_t', 'draw_mask_rect', 'draw_mask_rect_dsc_t', 'draw_rect', 'draw_rect_dsc_t', 'draw_sw_blend_dsc_t', 'draw_sw_custom_blend_handler_t', 'draw_sw_deinit', 'draw_sw_get_blend_handler', 'draw_sw_i1_convert_to_vtiled', 'draw_sw_i1_invert', 'draw_sw_i1_to_argb8888', 'draw_sw_init', 'draw_sw_mask_angle_param_cfg_t', 'draw_sw_mask_angle_param_t', 'draw_sw_mask_apply', 'draw_sw_mask_cleanup', 'draw_sw_mask_common_dsc_t', 'draw_sw_mask_deinit', 'draw_sw_mask_fade_param_cfg_t', 'draw_sw_mask_fade_param_t', 'draw_sw_mask_free_param', 'draw_sw_mask_init', 'draw_sw_mask_line_param_cfg_t', 'draw_sw_mask_line_param_t', 'draw_sw_mask_map_param_cfg_t', 'draw_sw_mask_map_param_t', 'draw_sw_mask_radius_circle_dsc_t', 'draw_sw_mask_radius_param_cfg_t', 'draw_sw_mask_radius_param_t', 'draw_sw_rgb565_swap', 'draw_sw_rotate', 'draw_sw_transform', 'draw_sw_unregister_blend_handler', 'draw_task_t', 'draw_triangle', 'draw_triangle_dsc_t', 'draw_unit_t', 'draw_wait_for_finish', 'dropdown', 'dropdown_class', 'dropdownlist_class', 'event_code_get_name', 'event_dsc_t', 'event_list_t', 'event_mark_deleted', 'event_register_id', 'event_t', 'flex_init', 'font_class_t', 'font_get_default', 'font_glyph_dsc_gid_t', 'font_glyph_dsc_t', 'font_info_t', 'font_montserrat_14', 'font_montserrat_16', 'font_montserrat_24', 'font_t', 'free', 'free_core', 'fs_deinit', 'fs_dir_t', 'fs_drv_t', 'fs_file_cache_t', 'fs_file_t', 'fs_get_drv', 'fs_get_ext', 'fs_get_last', 'fs_get_letters', 'fs_init', 'fs_is_ready', 'fs_memfs_init', 'fs_path_ex_t', 'fs_up', 'gd_GCE', 'gd_GIF', 'gd_Palette', 'gd_open_gif_data', 'gd_open_gif_file', 'gif', 'gif_class', 'grad_dsc_t', 'grad_stop_t', 'grid_fr', 'grid_init', 'group_by_index', 'group_create', 'group_deinit', 'group_focus_obj', 'group_get_count', 'group_get_default', 'group_init', 'group_remove_obj', 'group_swap_obj', 'group_t', 'hit_test_info_t', 'image', 'image_cache_data_t', 'image_class', 'image_decoder_args_t', 'image_decoder_dsc_t', 'image_decoder_t', 'image_dsc_t', 'image_header_t', 'imagebutton', 'imagebutton_class', 'imgfont_create', 'imgfont_destroy', 'indev_active', 'indev_create', 'indev_data_t', 'indev_get_active_obj', 'indev_keypad_t', 'indev_pointer_t', 'indev_read_timer_cb', 
    'indev_scroll_get_snap_dist', 'indev_search_obj', 'indev_t', 'init', 'inv_area', 'is_initialized', 'iter_create', 'iter_t', 'keyboard', 'keyboard_class', 'label', 'label_class', 'layer_bottom', 'layer_sys', 'layer_t', 'layer_top', 'layout_apply', 'layout_deinit', 'layout_dsc_t', 'layout_init', 'layout_register', 'led', 'led_class', 'line', 'line_class', 'list_button_class', 'list_class', 'list_text_class', 'll_t', 'lock', 'lock_isr', 'lodepng_deinit', 'lodepng_init', 'malloc', 'malloc_core', 'malloc_zeroed', 'matrix_t', 'mem_add_pool', 'mem_deinit', 'mem_init', 'mem_monitor_t', 'mem_remove_pool', 'mem_test', 'mem_test_core', 'memcmp', 'memcpy', 'memmove', 'memset', 'memzero', 'menu', 'menu_class', 'menu_cont', 'menu_cont_class', 'menu_main_cont_class', 'menu_main_header_cont_class', 'menu_page', 'menu_page_class', 'menu_section', 'menu_section_class', 'menu_separator', 'menu_separator_class', 'menu_sidebar_cont_class', 'menu_sidebar_header_cont_class', 'mp_lv_deinit_gc', 'mp_lv_init_gc', 'msgbox', 'msgbox_backdrop_class', 'msgbox_class', 'msgbox_content_class', 'msgbox_footer_button_class', 'msgbox_footer_class', 'msgbox_header_button_class', 'msgbox_header_class', 'mutex_delete', 'mutex_init', 'mutex_lock', 'mutex_lock_isr', 'mutex_unlock', 'obj', 'obj_class', 'obj_class_t', 'obj_style_transition_dsc_t', 'observer_t', 'os_get_idle_percent', 'os_init', 'palette_darken', 'palette_lighten', 'palette_main', 'pct', 'pct_to_px', 'point_precise_t', 'point_t', 'qrcode', 'qrcode_class', 'rand', 'rand_set_seed', 'rb_node_t', 'rb_t', 'realloc', 'realloc_core', 'reallocf', 'refr_deinit', 'refr_get_disp_refreshing', 'refr_init', 'refr_now', 'refr_set_disp_refreshing', 'roller', 'roller_class', 'scale', 'scale_class', 'scale_section_t', 'screen_active', 'screen_load', 'screen_load_anim', 'slider', 'slider_class', 'snapshot_create_draw_buf', 'snapshot_free', 'snapshot_reshape_draw_buf', 'snapshot_take', 'snapshot_take_to_buf', 'snapshot_take_to_draw_buf', 'span_coords_t', 'span_stack_deinit', 'span_stack_init', 'span_t', 'spangroup', 'spangroup_class', 'spinbox', 'spinbox_class', 'spinner', 'spinner_class', 'sqr', 'sqrt', 'sqrt32', 'sqrt_res_t', 'strcat', 'strchr', 'strcmp', 'strcpy', 'strdup', 'streq', 'strlcpy', 'strlen', 'strncat', 'strncmp', 'strncpy', 'strndup', 'strnlen', 'style_const_prop_id_inv', 'style_get_num_custom_props', 'style_get_prop_group', 'style_prop_get_default', 'style_prop_has_flag', 'style_prop_lookup_flags', 'style_register_prop', 'style_t', 'style_transition_dsc_t', 'style_value_t', 'subject_t', 'subject_value_t', 'swap_bytes_16', 'swap_bytes_32', 'switch', 'switch_class', 'table', 'table_class', 'tabview', 'tabview_class', 'task_handler', 'text_cut', 'text_encoded_letter_next_2', 'text_get_next_line', 'text_get_size', 'text_get_width', 'text_get_width_with_flags', 'text_ins', 'text_is_a_word', 'text_is_break_char', 'text_is_cmd', 'text_is_marker', 'textarea', 'textarea_class', 'theme_apply', 'theme_default_deinit', 'theme_default_get', 'theme_default_init', 'theme_default_is_inited', 'theme_get_color_primary', 'theme_get_color_secondary', 'theme_get_font_large', 'theme_get_font_normal', 'theme_get_font_small', 'theme_get_from_obj', 'theme_t', 'thread_delete', 'thread_init', 'thread_sync_delete', 'thread_sync_init', 'thread_sync_signal', 'thread_sync_signal_isr', 'thread_sync_wait', 'tick_elaps', 'tick_get', 'tick_inc', 'tick_set_cb', 'tick_state_t', 'tileview', 'tileview_class', 'tileview_tile_class', 'timer_core_deinit', 'timer_core_init', 'timer_create', 'timer_create_basic', 'timer_enable', 'timer_get_idle', 'timer_get_time_until_next', 'timer_handler', 'timer_handler_run_in_period', 'timer_handler_set_resume_cb', 'timer_periodic_handler', 'timer_state_t', 'timer_t', 'tjpgd_deinit', 'tjpgd_init', 'tree_class_t', 'tree_node_class', 'tree_node_t', 'trigo_cos', 'trigo_sin', 'unlock', 'utils_bsearch', 'version_info', 'version_major', 'version_minor', 'version_patch', 'win', 'win_class', 'zalloc']
>>> lv.screen_
screen_active


['__class__', '__name__', 'CLASS_EDITABLE', 'CLASS_GROUP_DEF', 'CLASS_THEME_INHERITABLE', 'FLAG', 'POINT_TRANSFORM_FLAG', 'TREE_WALK', '__bases__', '__cast__', '__dict__', 'add_event_cb', 'add_flag', 'add_state', 'add_style', 'align', 'align_to', 'allocate_spec_attr', 'area_is_visible', 'bind_checked', 'bind_flag_if_eq', 'bind_flag_if_ge', 'bind_flag_if_gt', 'bind_flag_if_le', 'bind_flag_if_lt', 'bind_flag_if_not_eq', 'bind_state_if_eq', 'bind_state_if_ge', 'bind_state_if_gt', 'bind_state_if_le', 'bind_state_if_lt', 'bind_state_if_not_eq', 'calculate_ext_draw_size', 'calculate_style_text_align', 'center', 'check_type', 'class_create_obj', 'class_init_obj', 'clean', 'delete', 'delete_anim_completed_cb', 'delete_async', 'delete_delayed', 'destruct', 'dump_tree', 'enable_style_refresh', 'event_base', 'fade_in', 'fade_out', 'get_child', 'get_child_by_type', 'get_child_count', 'get_child_count_by_type', 'get_class', 'get_click_area', 'get_content_coords', 'get_content_height', 'get_content_width', 'get_coords', 'get_display', 'get_event_count', 'get_event_dsc', 'get_ext_draw_size', 'get_group', 'get_height', 'get_index', 'get_index_by_type', 'get_layer_type', 'get_local_style_prop', 'get_parent', 'get_screen', 'get_scroll_bottom', 'get_scroll_dir', 'get_scroll_end', 'get_scroll_left', 'get_scroll_right', 'get_scroll_snap_x', 'get_scroll_snap_y', 'get_scroll_top', 'get_scroll_x', 'get_scroll_y', 'get_scrollbar_area', 'get_scrollbar_mode', 'get_self_height', 'get_self_width', 'get_sibling', 'get_sibling_by_type', 'get_state', 'get_style_align', 'get_style_anim', 'get_style_anim_duration', 'get_style_arc_color', 'get_style_arc_color_filtered', 'get_style_arc_image_src', 'get_style_arc_opa', 'get_style_arc_rounded', 'get_style_arc_width', 'get_style_base_dir', 'get_style_bg_color', 'get_style_bg_color_filtered', 'get_style_bg_grad', 'get_style_bg_grad_color', 'get_style_bg_grad_color_filtered', 'get_style_bg_grad_dir', 'get_style_bg_grad_opa', 'get_style_bg_grad_stop', 'get_style_bg_image_opa', 'get_style_bg_image_recolor', 'get_style_bg_image_recolor_filtered', 'get_style_bg_image_recolor_opa', 'get_style_bg_image_src', 'get_style_bg_image_tiled', 'get_style_bg_main_opa', 'get_style_bg_main_stop', 'get_style_bg_opa', 'get_style_bitmap_mask_src', 'get_style_blend_mode', 'get_style_border_color', 'get_style_border_color_filtered', 'get_style_border_opa', 'get_style_border_post', 'get_style_border_side', 'get_style_border_width', 'get_style_clip_corner', 'get_style_color_filter_dsc', 'get_style_color_filter_opa', 'get_style_flex_cross_place', 'get_style_flex_flow', 'get_style_flex_grow', 'get_style_flex_main_place', 'get_style_flex_track_place', 'get_style_grid_cell_column_pos', 'get_style_grid_cell_column_span', 'get_style_grid_cell_row_pos', 'get_style_grid_cell_row_span', 'get_style_grid_cell_x_align', 'get_style_grid_cell_y_align', 'get_style_grid_column_align', 'get_style_grid_column_dsc_array', 'get_style_grid_row_align', 'get_style_grid_row_dsc_array', 'get_style_height', 'get_style_image_opa', 'get_style_image_recolor', 'get_style_image_recolor_filtered', 'get_style_image_recolor_opa', 'get_style_layout', 'get_style_length', 'get_style_line_color', 'get_style_line_color_filtered', 'get_style_line_dash_gap', 'get_style_line_dash_width', 'get_style_line_opa', 'get_style_line_rounded', 'get_style_line_width', 'get_style_margin_bottom', 'get_style_margin_left', 'get_style_margin_right', 'get_style_margin_top', 'get_style_max_height', 'get_style_max_width', 'get_style_min_height', 'get_style_min_width', 'get_style_opa', 'get_style_opa_layered', 'get_style_opa_recursive', 'get_style_outline_color', 'get_style_outline_color_filtered', 'get_style_outline_opa', 'get_style_outline_pad', 'get_style_outline_width', 'get_style_pad_bottom', 'get_style_pad_column', 'get_style_pad_left', 'get_style_pad_radial', 'get_style_pad_right', 'get_style_pad_row', 'get_style_pad_top', 'get_style_prop', 'get_style_radial_offset', 'get_style_radius', 'get_style_recolor', 'get_style_recolor_opa', 'get_style_recolor_recursive', 'get_style_rotary_sensitivity', 'get_style_shadow_color', 'get_style_shadow_color_filtered', 'get_style_shadow_offset_x', 'get_style_shadow_offset_y', 'get_style_shadow_opa', 'get_style_shadow_spread', 'get_style_shadow_width', 'get_style_space_bottom', 'get_style_space_left', 'get_style_space_right', 'get_style_space_top', 'get_style_text_align', 'get_style_text_color', 'get_style_text_color_filtered', 'get_style_text_decor', 'get_style_text_font', 'get_style_text_letter_space', 'get_style_text_line_space', 'get_style_text_opa', 'get_style_text_outline_stroke_color', 'get_style_text_outline_stroke_color_filtered', 'get_style_text_outline_stroke_opa', 'get_style_text_outline_stroke_width', 'get_style_transform_height', 'get_style_transform_pivot_x', 'get_style_transform_pivot_y', 'get_style_transform_rotation', 'get_style_transform_scale_x', 'get_style_transform_scale_x_safe', 'get_style_transform_scale_y', 'get_style_transform_scale_y_safe', 'get_style_transform_skew_x', 'get_style_transform_skew_y', 'get_style_transform_width', 'get_style_transition', 'get_style_translate_radial', 'get_style_translate_x', 'get_style_translate_y', 'get_style_width', 'get_style_x', 'get_style_y', 'get_transform', 'get_transformed_area', 'get_user_data', 'get_width', 'get_x', 'get_x2', 'get_x_aligned', 'get_y', 'get_y2', 'get_y_aligned', 'has_class', 'has_flag', 'has_flag_any', 'has_state', 'has_style_prop', 'hit_test', 'init_draw_arc_dsc', 'init_draw_image_dsc', 'init_draw_label_dsc', 'init_draw_line_dsc', 'init_draw_rect_dsc', 'invalidate', 'invalidate_area', 'is_editable', 'is_group_def', 'is_layout_positioned', 'is_scrolling', 'is_valid', 'is_visible', 'mark_layout_as_dirty', 'move_background', 'move_children_by', 'move_foreground', 'move_to', 'move_to_index', 'null_on_delete', 'readjust_scroll', 'redraw', 'refr_pos', 'refr_size', 'refresh_ext_draw_size', 'refresh_self_size', 'refresh_style', 'remove_event', 'remove_event_cb', 'remove_event_cb_with_user_data', 'remove_event_dsc', 'remove_flag', 'remove_from_subject', 'remove_local_style_prop', 'remove_state', 'remove_style', 'remove_style_all', 'replace_style', 'report_style_change', 'reset_transform', 'scroll_by', 'scroll_by_bounded', 'scroll_by_raw', 'scroll_to', 'scroll_to_view', 'scroll_to_view_recursive', 'scroll_to_x', 'scroll_to_y', 'scrollbar_invalidate', 'send_event', 'set_align', 'set_content_height', 'set_content_width', 'set_ext_click_area', 'set_flag', 'set_flex_align', 'set_flex_flow', 'set_flex_grow', 'set_grid_align', 'set_grid_cell', 'set_grid_dsc_array', 'set_height', 'set_layout', 'set_local_style_prop', 'set_parent', 'set_pos', 'set_scroll_dir', 'set_scroll_snap_x', 'set_scroll_snap_y', 'set_scrollbar_mode', 'set_size', 'set_state', 'set_style_align', 'set_style_anim', 'set_style_anim_duration', 'set_style_arc_color', 'set_style_arc_image_src', 'set_style_arc_opa', 'set_style_arc_rounded', 'set_style_arc_width', 'set_style_base_dir', 'set_style_bg_color', 'set_style_bg_grad', 'set_style_bg_grad_color', 'set_style_bg_grad_dir', 'set_style_bg_grad_opa', 'set_style_bg_grad_stop', 'set_style_bg_image_opa', 'set_style_bg_image_recolor', 'set_style_bg_image_recolor_opa', 'set_style_bg_image_src', 'set_style_bg_image_tiled', 'set_style_bg_main_opa', 'set_style_bg_main_stop', 'set_style_bg_opa', 'set_style_bitmap_mask_src', 'set_style_blend_mode', 'set_style_border_color', 'set_style_border_opa', 'set_style_border_post', 'set_style_border_side', 'set_style_border_width', 'set_style_clip_corner', 'set_style_color_filter_dsc', 'set_style_color_filter_opa', 'set_style_flex_cross_place', 'set_style_flex_flow', 'set_style_flex_grow', 'set_style_flex_main_place', 'set_style_flex_track_place', 'set_style_grid_cell_column_pos', 'set_style_grid_cell_column_span', 'set_style_grid_cell_row_pos', 'set_style_grid_cell_row_span', 'set_style_grid_cell_x_align', 'set_style_grid_cell_y_align', 'set_style_grid_column_align', 'set_style_grid_column_dsc_array', 'set_style_grid_row_align', 'set_style_grid_row_dsc_array', 'set_style_height', 'set_style_image_opa', 'set_style_image_recolor', 'set_style_image_recolor_opa', 'set_style_layout', 'set_style_length', 'set_style_line_color', 'set_style_line_dash_gap', 'set_style_line_dash_width', 'set_style_line_opa', 'set_style_line_rounded', 'set_style_line_width', 'set_style_margin_all', 'set_style_margin_bottom', 'set_style_margin_hor', 'set_style_margin_left', 'set_style_margin_right', 'set_style_margin_top', 'set_style_margin_ver', 'set_style_max_height', 'set_style_max_width', 'set_style_min_height', 'set_style_min_width', 'set_style_opa', 'set_style_opa_layered', 'set_style_outline_color', 'set_style_outline_opa', 'set_style_outline_pad', 'set_style_outline_width', 'set_style_pad_all', 'set_style_pad_bottom', 'set_style_pad_column', 'set_style_pad_gap', 'set_style_pad_hor', 'set_style_pad_left', 'set_style_pad_radial', 'set_style_pad_right', 'set_style_pad_row', 'set_style_pad_top', 'set_style_pad_ver', 'set_style_radial_offset', 'set_style_radius', 'set_style_recolor', 'set_style_recolor_opa', 'set_style_rotary_sensitivity', 'set_style_shadow_color', 'set_style_shadow_offset_x', 'set_style_shadow_offset_y', 'set_style_shadow_opa', 'set_style_shadow_spread', 'set_style_shadow_width', 'set_style_size', 'set_style_text_align', 'set_style_text_color', 'set_style_text_decor', 'set_style_text_font', 'set_style_text_letter_space', 'set_style_text_line_space', 'set_style_text_opa', 'set_style_text_outline_stroke_color', 'set_style_text_outline_stroke_opa', 'set_style_text_outline_stroke_width', 'set_style_transform_height', 'set_style_transform_pivot_x', 'set_style_transform_pivot_y', 'set_style_transform_rotation', 'set_style_transform_scale', 'set_style_transform_scale_x', 'set_style_transform_scale_y', 'set_style_transform_skew_x', 'set_style_transform_skew_y', 'set_style_transform_width', 'set_style_transition', 'set_style_translate_radial', 'set_style_translate_x', 'set_style_translate_y', 'set_style_width', 'set_style_x', 'set_style_y', 'set_transform', 'set_user_data', 'set_width', 'set_x', 'set_y', 'stop_scroll_anim', 'style_apply_color_filter', 'style_apply_recolor', 'style_create_transition', 'style_deinit', 'style_get_selector_part', 'style_get_selector_state', 'style_init', 'style_state_compare', 'swap', 'transform_point', 'transform_point_array', 'tree_walk', 'update_layer_type', 'update_layout', 'update_snap']
