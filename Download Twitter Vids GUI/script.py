import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(label="Example Window", tag="Primary Window"):
    dpg.add_text("Link the twitter video here: ")
    dpg.add_input_text()
    dpg.add_button(label="Download")
    
dpg.create_viewport(title='Custom Title', width=300, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()