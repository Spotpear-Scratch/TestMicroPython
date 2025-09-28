# Required imports
from spotpear import *
import random



# Mapping ST7735
import machine
import st77xx
import lvgl as lv
import machine
#from machine import Pin

# Define the callback function to be called after 5 seconds
def on_timer_trigger_timer1(timer):
    print("Timer 1 expired! Calling the next function...")


# FIXME: spotpear.timer1, ...timer2, ... 
#        timer = Timer(-1)  # -1 means we're using a virtual timer
def create_timer( timer, _period = 5000 ):
    # Create a one-shot timer that triggers after 5000 milliseconds (5 seconds)
    if timer == 1:
        spotpear.timer1.init(mode=Timer.ONE_SHOT, period=_period, callback=on_timer_trigger_timer1)


def init_display():
    spi = machine.SPI( 1, baudrate=40_000_000, polarity=0, phase=0, sck=machine.Pin(3, machine.Pin.OUT), mosi=machine.Pin(4, machine.Pin.OUT), )
    disp = st77xx.St7735(rot=st77xx.ST77XX_INV_LANDSCAPE,res=(128,128), model='redtab', spi=spi, cs=2, dc=0, rst=5, rp2_dma=None, )
    scr = lv.obj()
    scr.set_style_bg_color(lv.color_hex(0x003a57), lv.PART.MAIN)
    lv.screen_load(scr)

def clear_screen():
    scr = lv.screen_active()
    scr.clean()
    scr.set_style_bg_color(lv.color_hex(0x003a57), lv.PART.MAIN)

def screen_background_color(_color=0x003a57):
    scr = lv.screen_active()
    scr.set_style_bg_color(lv.color_hex(_color), lv.PART.MAIN)
    return scr

def draw_rectangle(x=10, y=10, width=20, height=20, _color=0x00ff00):
    scr = lv.screen_active()
    color = lv.color_hex(_color)
    rect = lv.obj(scr)
    rect.set_size(width, height)
    rect.set_pos(x, y)
    rect.set_style_bg_color(color, 0)
    return rect

def draw_line(x1=10, y1=10, x2=50, y2=50, _color=0x0000ff, width=2):
    scr = lv.screen_active()
    color = lv.color_hex(_color)
    line = lv.line(scr)
    line.set_points([lv.point_precise_t({"x": x1, "y": y1}), lv.point_precise_t({"x": x2, "y": y2})],2)
    line.set_style_line_color(color, 0)
    line.set_style_line_width(width, 0)
    return line


def draw_circle(x=10, y=10, radius=10, _color=0xff0000):
    scr = lv.screen_active()
    color = lv.color_hex(_color)
    circle = lv.obj(scr)
    circle.set_size(radius * 2, radius * 2)
    circle.set_pos(x - radius, y - radius)
    circle.set_style_bg_color(color, 0)
    circle.set_style_radius(lv.RADIUS_CIRCLE, 0)
    return circle



def display_text_at_position(label_text="Hello, World!", x=10, y=10, font=lv.font_montserrat_24):
    screen = lv.screen_active()
    label = lv.label(screen)
    lv.label.set_text(label, label_text)
    label.set_pos(label, x, y)
    label_style = lv.style_t()
    label_style.init()
    label_style.set_text_font(font)
    label.add_style(label_style, 0)


def display_text_grid(square_size=50):
    screen = lv.screen_active()
    # Enable grid layout globally if not already enabled.
    # Note: This is often done in a configuration file (lv_conf.h)
    # but for MicroPython, you set it on the object directly.
    # We will use hard-coded track sizes instead.
    # Describe the grid layout for 5 rows and 5 columns
    # Using fixed pixel sizes for simplicity.
    col_dsc = [square_size] * 5 + [lv.GRID_TEMPLATE_LAST]
    row_dsc = [square_size] * 5 + [lv.GRID_TEMPLATE_LAST]
    # Create a parent object to hold the grid
    grid_container = lv.obj(screen)
    lv.obj.set_size(grid_container, 5 * square_size, 5 * square_size)
    lv.obj.center(grid_container)
    lv.obj.set_layout(grid_container, lv.LAYOUT.GRID)
    lv.obj.remove_flag(grid_container, lv.obj.FLAG.SCROLLABLE)
    lv.obj.set_style_pad_all(grid_container, 2, 0) # Add padding for spacing
    lv.obj.set_grid_dsc_array(grid_container, col_dsc, row_dsc)
    # Add zero padding to our label
    label_style = lv.style_t()
    label_style.init()
    #label_style.set_text_font(font)
    label_style.set_pad_all(0)    
    # Loop through the 5x5 array and create a square for each element
    for row_idx in range(5):
        for col_idx in range(5):
            # Create a simple object (like a panel) for the square
            square_obj = lv.obj(grid_container)
            lv.obj.set_style_bg_color(square_obj, lv.color_make(row_idx * 50, 255 - col_idx * 50, 100), 0)
            lv.obj.remove_flag(square_obj, lv.obj.FLAG.SCROLLABLE)
            lv.obj.set_grid_cell(
                square_obj,
                lv.GRID_ALIGN.STRETCH, col_idx, 1, # Align and span 1 column
                lv.GRID_ALIGN.STRETCH, row_idx, 1  # Align and span 1 row
            )
            # Optional: Add text to display the array value
            # This is a simple example and might need adjustments
            # based on your specific data type and display requirements.
            label = lv.label(square_obj)
            lv.label.set_text(label, "A")
            #lv.obj.center(label)
            #lv.obj.add_style(label, label_style, 0)


def display_colored_grid_v1(
    array_data,
    bg_color_hex,
    square_color_hex,
    screen_width,
    screen_height,
    border_size,
):
    # Get the active screen and set the background color.
    screen = lv.screen_active()
    lv.obj.set_style_bg_color(screen, lv.color_hex(bg_color_hex), lv.PART.MAIN)
    # Calculate the size of each square based on screen dimensions and borders
    total_borders = 6 * border_size  # 5 squares + 6 borders (including outer edges)
    square_size_w = (screen_width - total_borders) // 5
    square_size_h = (screen_height - total_borders) // 5
    square_size = min(square_size_w, square_size_h)
    # Describe the grid layout for 5 rows and 5 columns
    col_dsc = [square_size] * 5 + [lv.GRID_TEMPLATE_LAST]
    row_dsc = [square_size] * 5 + [lv.GRID_TEMPLATE_LAST]
    # Create a parent object (container) for the grid
    grid_container = lv.obj(screen)
    lv.obj.set_size(
        grid_container,
        5 * square_size + 4 * border_size,
        5 * square_size + 4 * border_size,
    )
    lv.obj.center(grid_container)
    lv.obj.set_layout(grid_container, lv.LAYOUT.GRID)
    # Set padding (the gap) between the grid items.
    lv.obj.set_style_pad_row(grid_container, border_size, 0)
    lv.obj.set_style_pad_column(grid_container, border_size, 0)
    lv.obj.set_style_pad_all(grid_container, border_size, 0)
    lv.obj.set_grid_dsc_array(grid_container, col_dsc, row_dsc)
    # Loop through the 5x5 array and create a square for each element
    for row_idx in range(5):
        for col_idx in range(5):
            # Create a simple object (square) within the grid container
            square_obj = lv.obj(grid_container)
            # Set the color based on the array value
            if array_data[row_idx][col_idx] == 1:
                lv.obj.set_style_bg_color(square_obj, lv.color_hex(square_color_hex), lv.PART.MAIN)
            # Place the square in the correct grid cell
            lv.obj.set_grid_cell(
                square_obj,
                lv.GRID_ALIGN.STRETCH,
                col_idx,
                1,
                lv.GRID_ALIGN.STRETCH,
                row_idx,
                1,
            )



def display_colored_grid(
    array_data,
    bg_color_hex,
    square_color_hex,
    screen_width,
    screen_height,
    border_size,
):
    # Get the active screen and set the background color.
    screen = lv.screen_active()
    lv.obj.set_style_bg_color(screen, lv.color_hex(bg_color_hex), 0)
    # Calculate the size of each square based on screen dimensions and borders.
    # We account for 5 squares and 6 borders (5 gaps + 2 outer edges).
    square_side = (min(screen_width, screen_height) - (6 * border_size)) // 5
    # Create a container to hold the squares and center it.
    # This prevents the grid from being misaligned if a border size is specified.
    grid_width = 5 * square_side + 4 * border_size
    grid_height = 5 * square_side + 4 * border_size
    container = lv.obj(screen)
    lv.obj.set_size(container, grid_width, grid_height)
    lv.obj.center(container)
    # Remove any default padding from the container
    lv.obj.set_style_pad_all(container, 0, 0)
    lv.obj.set_style_bg_opa(container, 0, 0) # Make container transparent
    # Loop through the 5x5 array and create and position each square.
    for row_idx in range(5):
        for col_idx in range(5):
            # Calculate the x and y position for the current square.
            x_pos = col_idx * (square_side + border_size)
            y_pos = row_idx * (square_side + border_size)
            # Create the square object as a child of the container.
            square_obj = lv.obj(container)
            lv.obj.set_size(square_obj, square_side, square_side)
            lv.obj.set_pos(square_obj, x_pos, y_pos)
            # Set the color based on the array value.
            if array_data[row_idx][col_idx] == 1:
                lv.obj.set_style_bg_color(square_obj, lv.color_hex(square_color_hex), lv.PART.MAIN)
            else:
                # Optionally, set a specific "off" color or make it invisible.
                lv.obj.set_style_bg_color(square_obj, lv.color_hex(bg_color_hex), lv.PART.MAIN)




def display_colored_grid_manual(
    array_data,
    bg_color_hex,
    square_color_hex,
    screen_width,
    screen_height,
    border_size,
):
    # Get the active screen and set the background color.
    screen = lv.screen_active()
    lv.obj.set_style_bg_color(screen, lv.color_hex(bg_color_hex), 0)
    # Calculate the size of each square based on screen dimensions and borders.
    square_side = (min(screen_width, screen_height) - (6 * border_size)) // 5
    # Create a container to hold the squares and center it.
    grid_width = 5 * square_side + 4 * border_size
    grid_height = 5 * square_side + 4 * border_size
    container = lv.obj(screen)
    lv.obj.set_size(container, grid_width, grid_height)
    lv.obj.center(container)
    lv.obj.set_style_pad_all(container, lv.OPA.TRANSP, 0)
    # The background of an object is transparent by default if no style is set,
    # so we don't need to explicitly set the opacity.
    # Loop through the 5x5 array and create and position each square.
    for row_idx in range(5):
        for col_idx in range(5):
            # Calculate the x and y position for the current square.
            x_pos = col_idx * (square_side + border_size)
            y_pos = row_idx * (square_side + border_size)
            # Create the square object as a child of the container.
            square_obj = lv.obj(container)
            lv.obj.set_size(square_obj, square_side, square_side)
            lv.obj.set_pos(square_obj, x_pos, y_pos)
            # Set the color based on the array value.
            if array_data[row_idx][col_idx] == 1:
                lv.obj.set_style_bg_color(square_obj, lv.color_hex(square_color_hex), 0)
            else:
                # Optionally, set a specific "off" color or inherit the background color.
                lv.obj.set_style_bg_color(square_obj, lv.color_hex(bg_color_hex), 0)





def setLED( boolean ):
    led = Pin(11, Pin.OUT)
    if boolean == 0:
        led.off()
    else:
        led.on()

def getButton( button_number ):
    button1 = Pin(8, Pin.IN, Pin.PULL_UP)
    button2 = Pin(10, Pin.IN, Pin.PULL_UP)
    if button_number == 1:
        return button1.value()
    elif button_number == 2:
        return button2.value()
    else:
        return None

def setPixel( x=0, y=0, color=lv.color_hex(0xff0000)  ):
    scr = lv.lv.screen_active()
    pixel = lv.obj(scr)
    lv.obj.set_size(pixel, 10, 10)
    lv.obj.set_pos(pixel, x, y)
    lv.obj.set_style_bg_color(pixel, color, 0)


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

display_colored_grid_v1(
    example_array,
    BACKGROUND_COLOR,
    SQUARE_COLOR,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BORDER_SIZE,
)

display_colored_grid(
    example_array,
    BACKGROUND_COLOR,
    SQUARE_COLOR,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BORDER_SIZE,
)

display_colored_grid_manual(
    example_array,
    BACKGROUND_COLOR,
    SQUARE_COLOR,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BORDER_SIZE,
)





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
