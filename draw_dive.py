
from tkinter import *

import dive_def

class Dive_drawing:
    def __init__(self):
        self.profondeur_1=40
        self.profondeur_2=20
        self.duree_1=20
        self.duree_2=30
        self.intervalle=120

        self.fenetre = Tk()
        self.fenetre.title("Calcul de palier selon tables MN90-FFESSM")
        self.journee_plongee=dive_def.Profile_dive()


    def create_interface(self):

        self.fenetre.Frame_top = Frame(self.fenetre, borderwidth=2, width=550, height=400, relief=GROOVE, background='white')
        self.fenetre.Frame_top.pack(side=TOP, padx=5, pady=5)

        self.fenetre.Frame_bottom= Frame(self.fenetre, borderwidth=2, width=550, height=200, relief=GROOVE, background='white')
        self.fenetre.Frame_bottom.pack(side=BOTTOM, padx=5, pady=5)



        self.fenetre.Frame_top.Frame_Param = Frame(self.fenetre.Frame_top, borderwidth=0, width=150, height=400, relief=GROOVE, background='white')
        self.fenetre.Frame_top.Frame_Param.pack(side=LEFT,padx=0, pady=0)

        self.fenetre.Frame_top.Display = Frame(self.fenetre.Frame_top, borderwidth=0, width=400, height=400, relief=GROOVE, background='white')
        self.fenetre.Frame_top.Display.pack(side=RIGHT, padx=0, pady=0)


        self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE1 = Frame(self.fenetre.Frame_top.Frame_Param, width=150, height=150, background='white')
        self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE1.pack()
        self.fenetre.Frame_top.Frame_Param.Frame_Param_inter_DIVE = Frame(self.fenetre.Frame_top.Frame_Param, width=150, height=150, background='white')
        self.fenetre.Frame_top.Frame_Param.Frame_Param_inter_DIVE.pack()
        self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE2 = Frame(self.fenetre.Frame_top.Frame_Param, width=150, height=150, background='white')
        self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE2.pack()

        ###########################################################################################################
        #Paramêtre de la plongée 1
        label = Label(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE1, text="Plongee 1",anchor='n', background='white')
        label.pack()

        label = Label(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE1, text="Profondeur : ",anchor='nw', background='white')
        label.pack()


        display_text=StringVar()
        display_text.set(str(self.profondeur_1))
        self.profondeur_1_field = Entry(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE1, textvariable=display_text, width=30,justify='center')
        self.profondeur_1_field.pack()

        display_text=StringVar()
        display_text.set(str(self.duree_1))
        label = Label(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE1, text="Duree : ",anchor='nw', background='white')
        label.pack()
        self.duree_1_field = Entry(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE1, textvariable=display_text, width=30,justify='center')
        self.duree_1_field.pack()

        ###########################################################################################################
        #Paramêtre de la plongée 2
        label = Label(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE2, text="Plongee 2",anchor='nw', background='white')
        label.pack()

        label = Label(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE2, text="Profondeur : ",anchor='nw', background='white')
        label.pack()
        display_text=StringVar()
        display_text.set(str(self.profondeur_2))
        self.profondeur_2_field = Entry(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE2, textvariable=display_text, width=30,justify='center')
        self.profondeur_2_field.pack()
        label = Label(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE2, text="Duree : ",anchor='nw', background='white')
        label.pack()
        display_text=StringVar()
        display_text.set(str(self.duree_2))
        self.duree_2_field = Entry(self.fenetre.Frame_top.Frame_Param.Frame_Param_DIVE2, textvariable=display_text, width=30,justify='center')
        self.duree_2_field.pack()



        ###########################################################################################################

        label = Label(self.fenetre.Frame_top.Frame_Param.Frame_Param_inter_DIVE, text="Intervalle de Surface",anchor='nw', background='white')
        label.pack()


        display_text=StringVar()
        display_text.set(str(self.intervalle))
        self.intervalle_surface = Entry(self.fenetre.Frame_top.Frame_Param.Frame_Param_inter_DIVE, textvariable=display_text, width=30,justify='center')
        self.intervalle_surface.pack()


        self.actualisation = Button(self.fenetre.Frame_top.Frame_Param, text ="Actualiser", command = lambda : self.actualiser(), width=30,justify='center')
        self.actualisation.pack()


    def recuperer(self):
        self.profondeur_1=int(self.profondeur_1_field.get())
        self.profondeur_2=int(self.profondeur_2_field.get())
        self.duree_1=int(self.duree_1_field.get())
        self.duree_2=int(self.duree_2_field.get())
        self.intervalle=int(self.intervalle_surface.get())

        self.journee_plongee.plongee_1.profondeur=int(self.profondeur_1_field.get())
        self.journee_plongee.plongee_1.profondeur_calcul=int(self.profondeur_1_field.get())
        self.journee_plongee.plongee_1.duree=int(self.duree_1_field.get())
        self.journee_plongee.plongee_2.profondeur=int(self.profondeur_2_field.get())
        self.journee_plongee.plongee_2.profondeur_calcul=int(self.profondeur_2_field.get())
        self.journee_plongee.plongee_2.duree=int(self.duree_2_field.get())
        self.journee_plongee.intervalle=int(self.intervalle_surface.get())

        print('plongée 1 : profondeur' ,self.profondeur_1 ,'min')
        print('plongée 1 : durée' ,self.duree_1 ,'min')

        print('plongée 2 : profondeur' ,self.profondeur_2 ,'min')
        print('plongée 2 : durée' ,self.duree_2 ,'min')


    def runloop(self):
        self.fenetre.mainloop()

    def create_canvas(self):
        self.canvas = Canvas(self.fenetre.Frame_top.Display, width=400, height=400, background='white')

        self.affichage_width=400
        self.affichage_height=350
        self.current_x_coord=0
        self.current_y_coord=30

    #def display_dive(canvas,plongee,affichage_width,affichage_height,x_start,y_start):
    def display_dive(self,plongee,profondeur_max,total_time):

        x_start=self.current_x_coord
        y_start=self.current_y_coord

        profondeur_surface=y_start

        profondeur_P1=plongee.profondeur
        duree_fond=plongee.duree
        duree_palier12m=plongee.palier_12m
        duree_palier9m=plongee.palier_9m
        duree_palier6m=plongee.palier_6m
        duree_palier3m=plongee.palier_3m
        duree_totale_palier=duree_palier12m+duree_palier9m+duree_palier6m+duree_palier3m;

        duree_remontée_palier12m=(profondeur_P1-12)/15;
        duree_remontée_palier9m=3/6;
        duree_remontée_palier6m=3/6;
        duree_remontée_palier3m=3/6;
        duree_remontée_palier0m=3/6;
        duree_totale_ascension=duree_remontée_palier9m+duree_remontée_palier6m+duree_remontée_palier3m+duree_remontée_palier0m

        duree_totale_remonte=duree_totale_palier+duree_totale_ascension

        duree_total_plongée=duree_fond+duree_totale_remonte

        duree_totale=duree_total_plongée



        affichage_width = self.affichage_width*duree_totale/total_time
        affichage_height= self.affichage_height*profondeur_P1/profondeur_max

        print('Affichage de la plongee: ',plongee.nom)

        print('profondeur max journee: ',profondeur_max,'/temps : ',total_time)
        print('profondeur max plongée: ',profondeur_P1,'/temps : ',duree_totale)

        #descente
        coord_1=[x_start,y_start]
        coord_x=x_start+0
        coord_y=y_start+affichage_height*profondeur_P1/profondeur_P1
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('descente')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)
        #temps fonds
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_fond/duree_totale
        coord_y=coord_y
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('temps fonds')
        #('profondeur: ',coord_y,'/temps : ',coord_x)
        #remontee palier 12m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_remontée_palier12m/duree_totale
        coord_y=coord_y-affichage_height*(profondeur_P1-12)/profondeur_P1
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('remontee palier 12m')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)
        #palier 12m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_palier12m/duree_totale
        coord_y=coord_y
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('palier 9m')
        #print('profondeur: ',coord_y,'/temps : ',coord_y)
        #remontee palier 9m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_remontée_palier9m/duree_totale
        coord_y=coord_y-affichage_height*3/profondeur_P1
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('remontee palier 9m')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)
        #palier 9m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_palier9m/duree_totale
        coord_y=coord_y
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('palier 9m')
        #print('profondeur: ',coord_y,'/temps : ',coord_y)
        #remontee palier 6m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_remontée_palier6m/duree_totale
        coord_y=coord_y-affichage_height*3/profondeur_P1
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('remontee palier 6m')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)
        #palier 6m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_palier6m/duree_totale
        coord_y=coord_y
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('palier 6m')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)
        #remontee palier 3m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_remontée_palier3m/duree_totale
        coord_y=coord_y-affichage_height*3/profondeur_P1
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('remontee palier 3m')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)
        #palier 3m
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_palier3m/duree_totale
        coord_y=coord_y
        coord_2=[coord_x,coord_y]
        ligne = self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('palier 3m')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)
        #remontee surface
        coord_1=coord_2
        coord_x=coord_x+affichage_width*duree_remontée_palier0m/duree_totale
        coord_y=profondeur_surface
        coord_2=[coord_x,coord_y]
        ligne =self.canvas.create_line(coord_1,coord_2)
        self.canvas.pack()
        #print('remontee surface')
        #print('profondeur: ',coord_y,'/temps : ',coord_x)

        self.current_x_coord=coord_x


    def draw_surface(self,surface_time,total_time):
        print('affichage temps de surface')
        affichage_width = self.affichage_width
        affichage_height= self.affichage_height
        x_start=self.current_x_coord
        y_start=self.current_y_coord


        coord_1=[x_start,y_start]
        x_stop=x_start+affichage_width*surface_time/total_time
        coord_2=[x_stop,y_start]
        ligne =self.canvas.create_line(coord_1,coord_2)

        self.current_x_coord=x_stop



    ###########################################################################################################"
    def create_display_result(self):
        self.fenetre.Frame_bottom.Frame_DIVE1 = Frame(self.fenetre.Frame_bottom,borderwidth=0 , width=200, height=200, relief=GROOVE, background='white')
        self.fenetre.Frame_bottom.Frame_DIVE1.pack(side=LEFT,padx=5, pady=5)
        self.fenetre.Frame_bottom.Frame_inter_DIVE = Frame(self.fenetre.Frame_bottom,borderwidth=0 , width=200, height=200,  relief=GROOVE, background='white')
        self.fenetre.Frame_bottom.Frame_inter_DIVE.pack(side=LEFT,padx=5, pady=5)
        self.fenetre.Frame_bottom.Frame_DIVE2 = Frame(self.fenetre.Frame_bottom,borderwidth=0 , width=200, height=200,  relief=GROOVE, background='white')
        self.fenetre.Frame_bottom.Frame_DIVE2.pack(side=LEFT,padx=5, pady=5)


        self.zone_texte_plongee_1 = Canvas(self.fenetre.Frame_bottom.Frame_DIVE1, width=200, height=200, background='white')
        self.zone_texte_plongee_2 = Canvas(self.fenetre.Frame_bottom.Frame_DIVE2, width=200, height=200, background='white')
        self.zone_texte_interdive = Canvas(self.fenetre.Frame_bottom.Frame_inter_DIVE, width=200, height=200, background='white')


    def reset_display_result(self):

        self.zone_texte_plongee_1.delete(ALL)
        self.zone_texte_plongee_2.delete(ALL)
        self.zone_texte_interdive.delete(ALL)


        #self.zone_texte_plongee_1 = Canvas(self.fenetre.Frame_bottom.Frame_DIVE1, width=200, height=200, background='white')
        #self.zone_texte_plongee_2 = Canvas(self.fenetre.Frame_bottom.Frame_DIVE2, width=200, height=200, background='white')
        #self.zone_texte_interdive = Canvas(self.fenetre.Frame_bottom.Frame_inter_DIVE, width=200, height=200, background='white')

        self.canvas.delete(ALL)

        self.current_x_coord=0
        self.current_y_coord=30

    def display_dive_result(self,plongee,index):
        if index==1:
          canvas4display=self.zone_texte_plongee_1
        else:
          canvas4display=self.zone_texte_plongee_2


          canvas4display.delete(ALL)

        profondeur_P1=plongee.profondeur
        duree_fond=plongee.duree
        duree_palier12m=plongee.palier_12m
        duree_palier9m=plongee.palier_9m
        duree_palier6m=plongee.palier_6m
        duree_palier3m=plongee.palier_3m



        print('Rafraissimment des donnés de la plongée : ',plongee.nom)

        offset=20
        txt = canvas4display.create_text(10, offset, text=plongee.nom, font="Arial 10", fill="blue",anchor='sw')

        offset=offset+20
        text2display="Profondeur :%s m"% profondeur_P1
        txt =canvas4display.create_text(10, offset, text=text2display, font="Arial 10", fill="blue",anchor='sw')


        offset=offset+20
        text2display="Durée :%s min"% duree_fond
        txt = canvas4display.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')


        if duree_palier12m!=0:
            offset=offset+20
            text2display="Durée Palier 12m :%s min"% duree_palier12m
            txt = canvas4display.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')


        if duree_palier9m!=0:
            offset=offset+20
            text2display="Durée Palier 9m :%s min"% duree_palier9m
            txt = canvas4display.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')


        if duree_palier6m!=0:
            offset=offset+20
            text2display="Durée Palier 6m :%s min"% duree_palier6m
            txt = canvas4display.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')


        if duree_palier3m!=0:
            offset=offset+20
            text2display="Durée Palier 3m :%s min"% duree_palier3m
            txt = canvas4display.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')



        offset=offset+20
        text2display="Durée Total Remonte :%s min"% ( plongee.duree_totale-plongee.duree)
        txt = canvas4display.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')
        offset=offset+40
        text2display="Groupe Plongée Susccesive :%s "% plongee.groupe
        txt = canvas4display.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')




        canvas4display.pack(side=RIGHT)


    ###########################################################################################################"

    def display_interdive_result(self):


        #zone_texte = Canvas(self.zone_texte_interdive, width=200, height=200, background='white')
        zone_texte = self.zone_texte_interdive
        duree=self.journee_plongee.intervalle
        offset=20
        text2display="Intervalle de surface :%s min"% duree
        txt = zone_texte.create_text(10, offset, text=text2display, font="Arial 10", fill="blue",anchor='sw')



        if self.journee_plongee.intervalle<15:
            offset=offset+20
            text2display="Plongee Consecutive"
            txt = zone_texte.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')
        else :

            offset=offset+20
            text2display="Plongee Successive"
            txt = zone_texte.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')
            offset=offset+20
            text2display="Azote Residuel :%s "% (str(self.journee_plongee.azote_residuel/100))
            txt = zone_texte.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')
            offset=offset+20
            text2display="Majoration Plongee 2 :%s min"% self.journee_plongee.plongee_2.majoration
            txt = zone_texte.create_text(10, offset, text=text2display, font="Arial 8", fill="blue",anchor='sw')




        zone_texte.pack(side=RIGHT)

    def actualiser(self):
        self.recuperer()
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print('Nouvelle Journée')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')


        self.journee_plongee.plongee_1.nom="Matin"

        self.journee_plongee.plongee_1.calcul_palier()
        print('Temps de la plongée 1 ' ,self.journee_plongee.plongee_1.duree_totale ,'min')
        print('Profondeur de la plongée 1 ' ,self.journee_plongee.plongee_1.profondeur ,'m')
        print('plongée 1 : palier 12m' ,self.journee_plongee.plongee_1.palier_12m ,'min')
        print('plongée 1 : palier 9m' ,self.journee_plongee.plongee_1.palier_9m ,'min')
        print('plongée 1 : palier 6m' ,self.journee_plongee.plongee_1.palier_6m ,'min')
        print('plongée 1 : palier 3m' ,self.journee_plongee.plongee_1.palier_3m ,'min')

        #######################################"
        #Plongée 2
        self.journee_plongee.plongee_2.nom="Après Midi"



        #Calcul des majorations en fonction du type de plongée

        P1_profondeur=self.journee_plongee.plongee_1.profondeur
        P2_profondeur=self.journee_plongee.plongee_2.profondeur
        if P1_profondeur>P2_profondeur:
            profondeur_max=P1_profondeur
        else:
            profondeur_max=P2_profondeur

        if self.journee_plongee.intervalle<15:
            self.journee_plongee.plongee_2.majoration=self.journee_plongee.plongee_1.duree
            self.journee_plongee.plongee_2.profondeur_calcul=profondeur_max
        else:
            self.journee_plongee.calcul_azote_residuel()
        #plongee2.calc_duree_plongee()
        self.journee_plongee.plongee_2.calcul_palier()
        print('Temps de la plongée 2 ' ,self.journee_plongee.plongee_2.duree_totale ,'min')
        print('Profondeur de la plongée 2 ' ,self.journee_plongee.plongee_2.profondeur ,'m')
        print('plongée 2 : palier 12m' ,self.journee_plongee.plongee_2.palier_12m ,'min')
        print('plongée 2 : palier 9m' ,self.journee_plongee.plongee_2.palier_9m ,'min')
        print('plongée 2 : palier 6m' ,self.journee_plongee.plongee_2.palier_6m ,'min')
        print('plongée 2 : palier 3m' ,self.journee_plongee.plongee_2.palier_3m ,'min')

        #######################################"
        temps_surface=self.journee_plongee.intervalle
        #######################################"


        duree_avant_plongee=5
        duree_totale=duree_avant_plongee*2+self.journee_plongee.intervalle
        duree_totale=duree_totale+self.journee_plongee.plongee_1.duree_totale
        duree_totale=duree_totale+self.journee_plongee.plongee_2.duree_totale


        self.reset_display_result()
        self.draw_surface(5,duree_totale)
        self.display_dive(self.journee_plongee.plongee_1,profondeur_max,duree_totale)
        self.draw_surface(temps_surface,duree_totale)
        self.display_dive(self.journee_plongee.plongee_2,profondeur_max,duree_totale)
        self.draw_surface(5,duree_totale)

        self.display_dive_result(self.journee_plongee.plongee_1,1)
        self.display_dive_result(self.journee_plongee.plongee_2,2)
        self.display_interdive_result()
