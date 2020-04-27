
class Single_dive:
    def __init__(self,profondeur=20,duree=40):
        self.nom="Matin"
        self.profondeur = profondeur
        self.profondeur_calcul = profondeur
        self.duree = duree
        self.palier_12m=0
        self.palier_9m=0
        self.palier_6m=0
        self.palier_3m=0
        self.groupe=0
        self.majoration=0
        self.duree_totale=0
        self.hdebut=10
        self.hfin=10

    def calc_duree_plongee(self):
            profondeur=self.profondeur
            duree_fond=self.duree
            duree_palier12m=self.palier_12m
            duree_palier9m=self.palier_9m
            duree_palier6m=self.palier_6m
            duree_palier3m=self.palier_3m
            duree_totale_palier=duree_palier12m+duree_palier9m+duree_palier6m+duree_palier3m;


            temps_plongee_total=duree_fond+duree_totale_palier
            tps_remonte_palier=0
            distance_remonte=profondeur-12
            if duree_palier12m!=0:
                tps_remonte_palier=tps_remonte_palier+3/6
            else:
                distance_remonte=distance_remonte+3

            if duree_palier9m!=0:
                tps_remonte_palier=tps_remonte_palier+3/6
            else:
                distance_remonte=distance_remonte+3

            if duree_palier6m!=0:
                tps_remonte_palier=tps_remonte_palier+3/6
            else:
                distance_remonte=distance_remonte+3

            if duree_palier3m!=0:
                tps_remonte_palier=tps_remonte_palier+3/6
            else:
                distance_remonte=distance_remonte+3

            temps_remonte_fond=distance_remonte/15

            temps_plongee_total=round(temps_plongee_total+temps_remonte_fond+tps_remonte_palier)



            self.duree_totale= temps_plongee_total


    def calcul_palier(self):
        profondeur=self.profondeur_calcul
        duree_fond=self.duree+self.majoration
        table_MN90=open("tableMN90.txt", "r")

        table_MN90_line=table_MN90.readline()
        profondeur_table,duree_table,palier_12m,palier_9m,palier_6m,palier_3m,groupe=table_MN90_line.split(";")
        profondeur_table_int=int(profondeur_table)
        duree_table_int=int(duree_table)

        print('loop table')
        #while ((profondeur<profondeur_table_int) or (duree_fond<duree_table_int ) ) :
        while ((profondeur>profondeur_table_int) or (duree_fond>duree_table_int ) ) :
            table_MN90_line=table_MN90.readline()
            if (table_MN90_line == None ):
                print("Fin de fichier Table MN90")
                break

            profondeur_table, duree_table, palier_12m, palier_9m, palier_6m, palier_3m, groupe = table_MN90_line.split(";")
            profondeur_table_int=int(profondeur_table)
            duree_table_int=int(duree_table)


        if (table_MN90_line != None ):
            self.palier_12m=int(palier_12m)
            self.palier_9m=int(palier_9m)
            self.palier_6m=int(palier_6m)
            self.palier_3m=int(palier_3m)
            self.groupe=groupe


        self.calc_duree_plongee()
        table_MN90.close




class Profile_dive:
    def __init__(self):

        self.plongee_1 = Single_dive()
        self.plongee_2 = Single_dive()
        self.intervalle = 100
        self.start_time=10
        self.duree_totale=0
        self.azote_residuel=81

    # def MAJ_CallBack(self,fenetre):
    #     self.plongee_1.nom="Matin"
    #     self.plongee_1.profondeur=int(fenetre.profondeur_1.get())
    #     self.plongee_1.duree=int(fenetre.duree_1.get())
    #
    #     self.plongee_2.nom="Après Midi"
    #     self.plongee_2.profondeur=int(fenetre.profondeur_2.get())
    #     self.plongee_2.duree=int(fenetre.duree_2.get())
    #
    #     self.intervalle=int(fenetre.intervalle.get())
    #
    #     self.plongee_1.calcul_palier()
    #     self.plongee_2.calcul_palier()

    def calcul_azote_residuel(self):
        groupe=self.plongee_1.groupe[1]
        intervalle=self.intervalle
        profondeur_P2=self.plongee_2.profondeur

        self.azote_residuel=81


        print('Groupe : ',groupe)
        print('intervalle : ',intervalle)
        print('profondeur_P2 : ',profondeur_P2)

        #duree : 15min/30min/
        table_duree=[15,30,45,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630,660,690,720]
        table_profondeur=[12,15,18,20,22,25,28,30,32,35,38,40,42,45,48,50,52,55,58,60]

        AZote_tab = [0] *27
        Majoration_tab=[0] * 21

        Azote_residuel_file=open("Azote_Residuel.txt", "r")

        Azote_residuel_line=Azote_residuel_file.readline()
        AZote_tab=Azote_residuel_line.split(";")


        ###################################################################################
        #Reherche de l'azote residuel en fonction de l'intervalle de surface
        for index in range(1,16):
            Azote_residuel_line=Azote_residuel_file.readline()
            AZote_tab=Azote_residuel_line.split(";")
            print('Azote table Groupe',AZote_tab[0], ' longeur: ',len(AZote_tab[0]))
            if (str(AZote_tab[0])== str(groupe) ) :
                print('Azote table',AZote_tab)
                for index in range(0,25):
                    if table_duree[index]<intervalle:
                        azote_residuel=int(AZote_tab[index+1])

        Azote_residuel_file.close()




        print('Azote Residuel : ',azote_residuel)


        ###################################################################################
        #Reherche de la majoration en fonction de la profondeur de la plongee 2

        Majoration_file=open("Majoration.txt", "r")

        Majoration_line=Majoration_file.readline()
        Majoration_tab=Majoration_line.split(";")

        for index in range(1,19):
            Majoration_line=Majoration_file.readline()
            Majoration_tab=Majoration_line.split(";")
            if (int(Majoration_tab[0])>=azote_residuel ) :
                print('Majoration table',Majoration_tab)
                for index in range(1,20):
                    if table_profondeur[index-1]<=profondeur_P2:
                        majoration=int(Majoration_tab[index])
                break


        Majoration_file.close()




        print('Majoration : ',majoration)
        self.azote_residuel=azote_residuel
        self.plongee_2.majoration=majoration
