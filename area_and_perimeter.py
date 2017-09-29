import ui

def calculate_touch_up_inside(sender):
	length = float(view['length_text'].text)
	width = float(view['width_text'].text)
	
	view['area_label'].text = 'area: ' + str(length*width)
	view['perimeter_label'].text = 'perimeter: ' + str(length*2 + width*2)

view = ui.load_view()
view.present('sheet')
