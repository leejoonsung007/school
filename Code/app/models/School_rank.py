# class Pro2015(db.Model):
#     roll_number = db.Column(db.String(50), db.ForeignKey('school.roll_number'), primary_key=True)
#     #roll_number = db.Column(db.String(50), db.ForeignKey('school.roll_number'))
#     name = db.Column(db.String(50), nullable=False)
#     name2 = db.Column(db.String(50))
#     Number_who_sat_Leaving_Cert_2015 = db.Column(db.Integer)
#     UCD = db.Column(db.Integer)
#     TCD = db.Column(db.Integer)
#     DCU = db.Column(db.Integer)
#     UL = db.Column(db.Integer)
#     Maynooth_University = db.Column(db.Integer)
#     NUIG = db.Column(db.Integer)
#     UCC = db.Column(db.Integer)
#     St_Angela = db.Column(db.Integer)
#     QUB = db.Column(db.Integer)
#     UU = db.Column(db.Integer)
#     Blanch_IT = db.Column(db.Integer)
#     Nat_Col_of_Irl = db.Column(db.Integer)
#     DIT = db.Column(db.Integer)
#     Tallaght_IT = db.Column(db.Integer)
#     Cork_IT = db.Column(db.Integer)
#     Dundalk_IT = db.Column(db.Integer)
#     GMIT = db.Column(db.Integer)
#     IADT = db.Column(db.Integer)
#     IT_Carlow = db.Column(db.Integer)
#     IT_Sligo = db.Column(db.Integer)
#     IT_Tralee = db.Column(db.Integer)
#     IT_Letter_kenny = db.Column(db.Integer)
#     IT_Limerick = db.Column(db.Integer)
#     WIT = db.Column(db.Integer)
#     Marino_Instit_of_Ed = db.Column(db.Integer)
#     C_of_I_College_of_Ed = db.Column(db.Integer)
#     Mary_Immac = db.Column(db.Integer)
#     NCAD = db.Column(db.Integer)
#     RCSI = db.Column(db.Integer)
#     Shannon_College_of_Hotel_Management = db.Column(db.Integer)
#     Total_who_accepted_CAOplace = db.Column(db.Integer)
#     Total_progression = db.Column(db.DECIMAL(10,2)) #?
#
# class Rank2017(db.Model):
#     roll_number = db.Column(db.String(50), db.ForeignKey('school.roll_number'), primary_key=True)
#     #roll_number = db.Column(db.String(50), db.ForeignKey('school.roll_number'))
#     name = db.Column(db.String(50), nullable=False)
#     rank = db.Column(db.Integer)
#     p_rank =db.Column(db.Integer)
#     gender_type = db.Column(db.String(50))
#     at_university = db.Column(db.DECIMAL(10,2)) #?
#     at_third_level =db.Column(db.DECIMAL(10,2))
#     boy =db.Column(db.Integer)
#     girl =db.Column(db.Integer)
#     stu_tea_ratio =db.Column(db.DECIMAL(10,2)) #?