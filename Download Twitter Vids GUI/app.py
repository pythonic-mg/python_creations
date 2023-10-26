import dearpygui.dearpygui as dpg
import functions

dpg.create_context()

#create tags
input_id = dpg.generate_uuid()
button_id = dpg.generate_uuid()
text_id = dpg.generate_uuid()

with dpg.window(tag="Primary Window"):
    dpg.add_text("Link the twitter video here: ", indent=10, pos=[0,30])
    dpg.add_input_text(tag=input_id, indent=20, width=400, pos=[0,55])
    dpg.add_button(tag=button_id, label="Download", width=100, height=20, indent=20, pos=[0,75])
    dpg.add_text("", tag=text_id)
    

dpg.create_viewport(title='Downloader', width=300, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()