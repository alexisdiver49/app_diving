# coding: utf-8
#Authors alexis gabin

import draw_dive
import dive_def

from tkinter import *



main_app=draw_dive.Dive_drawing()
main_app.create_interface()



profondeur_surface=50  #position du pixel de surface


print('##########################################################""')
print('Debut du Programme')
print('##########################################################""')









#######################################"
#Plongée 1
# plongee1.nom="Matin"
# plongee1.profondeur=main_app.profondeur_1
# plongee1.duree=main_app.duree_1
#plongee1.palier_9m=5
#plongee1.palier_6m=10
#plongee1.palier_3m=15

#plongee1.calc_duree_plongee()
# plongee1.calcul_palier()
# print('Temps de la plongée 1 ' ,plongee1.duree_totale ,'min')
# print('plongée 1 : palier 12m' ,plongee1.palier_12m ,'min')
# print('plongée 1 : palier 9m' ,plongee1.palier_9m ,'min')
# print('plongée 1 : palier 6m' ,plongee1.palier_6m ,'min')
# print('plongée 1 : palier 3m' ,plongee1.palier_3m ,'min')

#######################################"
#Plongée 2
# plongee2.nom="Après Midi"
# plongee2.profondeur=main_app.profondeur_2
# plongee2.duree=main_app.duree_2
#plongee2.palier_9m=1
#plongee2.palier_6m=9
#plongee2.palier_3m=15


#plongee2.calc_duree_plongee()
# plongee2.calcul_palier()
# print('Temps de la plongée 2 ' ,plongee2.duree_totale ,'min')
# print('plongée 2 : palier 12m' ,plongee2.palier_12m ,'min')
# print('plongée 2 : palier 9m' ,plongee2.palier_9m ,'min')
# print('plongée 2 : palier 6m' ,plongee2.palier_6m ,'min')
# print('plongée 2 : palier 3m' ,plongee2.palier_3m ,'min')
#
# #######################################"
# temps_surface=main_app.intervalle
# #######################################"
# if plongee1.profondeur>plongee2.profondeur:
#     profondeur_max=plongee1.profondeur
# else:
#     profondeur_max=plongee2.profondeur
#
# profil_plongee.plongee1=plongee1
# profil_plongee.plongee2=plongee2
# profil_plongee.intervalle=temps_surface
#
#
# duree_avant_plongee=5
# duree_totale=duree_avant_plongee*2+temps_surface
# duree_totale=duree_totale+plongee1.duree_totale
# duree_totale=duree_totale+plongee2.duree_totale
# duree_totale=duree_totale+temps_surface
#
# main_app.profile_plongee()
main_app.create_canvas()
main_app.create_display_result()
# main_app.draw_surface(5,duree_totale)
# main_app.display_dive(plongee1,profondeur_max,duree_totale)
# main_app.draw_surface(temps_surface,duree_totale)
# main_app.display_dive(plongee2,profondeur_max,duree_totale)
# main_app.draw_surface(5,duree_totale)
#
# main_app.display_dive_result(plongee1,1)
# main_app.display_dive_result(plongee2,2)


main_app.actualiser()


# canvas = Canvas(main_app.Frame_top.Display, width=400, height=400, background='white')
#
# affichage_width=400
# affichage_height=350
# x_start=0
# y_start=30
#
#
# #Affichage des plongées
#
# #avant plongée
# coord_x=x_start
# coord_y=y_start
# coord_1=[coord_x,coord_y]
# coord_x=coord_x+affichage_width*duree_avant_plongee/duree_totale
# coord_2=[coord_x,coord_y]
# ligne = canvas.create_line(coord_1,coord_2)
# canvas.pack()
#
#
#
# #affichage de la plongée 1
# x_start=coord_x
# temps_affichage_plongee=plongee1.duree_totale/duree_totale*affichage_width
# profondeur_affichage=plongee1.profondeur/profondeur_max*affichage_height
# x_end=draw_dive.display_dive(canvas,plongee1,temps_affichage_plongee,profondeur_affichage,x_start,y_start)
#
# #intervalle de surface
# coord_x=x_end
# coord_y=y_start
# coord_1=[coord_x,coord_y]
# coord_x=coord_x+affichage_width*temps_surface/duree_totale
# coord_2=[coord_x,coord_y]
# ligne = canvas.create_line(coord_1,coord_2)
# canvas.pack()
#
# #affichage de la plongée 2
# x_start=coord_x
# temps_affichage_plongee=plongee2.duree_totale/duree_totale*affichage_width
# profondeur_affichage=plongee2.profondeur/profondeur_max*affichage_height
# x_end=draw_dive.display_dive(canvas,plongee2,temps_affichage_plongee,profondeur_affichage,x_start,y_start)
#
#
# #après plongée
# coord_x=x_end
# coord_y=y_start
# coord_1=[coord_x,coord_y]
# coord_x=coord_x+affichage_width*duree_avant_plongee/duree_totale
# coord_2=[coord_x,coord_y]
# ligne = canvas.create_line(coord_1,coord_2)
# canvas.pack()
#
#
# #affichage des paramètres de la plongée
# draw_dive.display_dive_result(fenetre.Frame_bottom.Frame_DIVE1,plongee1)
#
#
# # affichage de l'intervalle de surface
# draw_dive.display_interdive_result(fenetre.Frame_bottom.Frame_inter_DIVE,temps_surface)
#
#
# #affichage des paramètres de la plongée
# draw_dive.display_dive_result(fenetre.Frame_bottom.Frame_DIVE2,plongee2)
#
# func_dive.get_total_dive(fenetre)


main_app.runloop()
# fenetre.mainloop() # keep window open
##
##p = PanedWindow(Frame_ResultDisplay, orient=HORIZONTAL)
##p.pack(side=TOP, expand=Y, fill=BOTH , padx=100, pady=100)
##p.add(Label(p, text='plongee', background='blue', anchor=CENTER))
