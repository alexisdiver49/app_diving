# coding: utf-8
#Authors alexis gabin

import draw_dive
import dive_def

from tkinter import *



main_app=draw_dive.Dive_drawing()
main_app.create_interface()





print('##########################################################""')
print('Debut du Programme')
print('##########################################################""')



#
# main_app.profile_plongee()
main_app.create_canvas()
main_app.create_display_result()

main_app.actualiser()




main_app.runloop()
