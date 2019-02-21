class Config:
	SECRET_KEY = '04beccaf060f0a03ebfc301930fc1c30'
	#SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:rt_20@localhost/UniQx'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
