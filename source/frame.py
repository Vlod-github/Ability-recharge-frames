from PIL import Image
import math
import os


output_folder = 'frames'
if os.path.exists(output_folder):
	assert os.path.isdir(output_folder)
else:
	os.mkdir(output_folder)

size = (64, 64) # output frame size
x0, y0 = size[0]/2, size[1]/2

count_frames = 100 # number of frames
assert count_frames > 1

for i in range(count_frames):
	angle = i*(math.pi*2/count_frames)
	frame = Image.new('RGBA', size, 'black')
	frame_obj = frame.load()
	for x in range(size[0]):
		for y in range(size[1]):
			t_angle = math.atan2(y0-y, x0-x)
			if t_angle < 0:
				t_angle += 2*math.pi
			if t_angle < angle:
				frame_obj[x,y] = (0,0,0,0)
	frame = frame.rotate(270)
	frame.save(output_folder + f'/{i}.png')