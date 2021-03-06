from .insert_data_users import *

class user_info:

	def __init__(self,dbname):
		self.user = db(dbname)

	def identify_user(self,fingerprintID):
		userID = self.user.selectQuery('fingerprint',['ID'],['FINGERPRINT_ID = ' + str(fingerprintID)])
		if userID==[]:
			return None
		else:
			return userID[0][0]
	
	def getFingerID(self,userID):
		fingerID=self.user.selectQuery('fingerprint',['FINGERPRINT_ID'],['ID = ' + str(userID)])
		if fingerID==[]:
			return None
		else:
			return fingerID[0][0]

	def getUserID(self):
		userID = self.user.selectQuery('users',['ID'],['ID = (SELECT MAX(ID) FROM users)'])
		return userID[0][0]


	def get_user_info(self, id):
		user_list = self.user.selectQuery('users',['*'],['ID = ' + str(id)])
		user_info_list = [user_list[0][1],user_list[0][3],user_list[0][4],user_list[0][5],user_list[0][2],user_list[0][8],user_list[0][9],user_list[0][10]]
		return user_info_list

	def update_user_info(self, values, id):
		values[0] = "NAME = '" + values[0] + "'"
		values[1] = "PHONE_CALL = '" + values[1] + "'"
		values[2] = "PHONE_WHATSAPP = '" + values[2] + "'"
		values[3] = "ROOM_NO = '" + values[3] + "'"
		values[4] = "EMAIL_ID = '" + values[4] + "'"
		self.user.updateQuery('users',values, ['ID = ' + str(id)])



# def main():
# 	obj = user_info('SIMS.db')
# 	# user_info_list = obj.get_user_info(1)
# 	#print user_info_list
# 	# obj.update_user_info(["yashdeep thorat",'9010712068','9665333384','BM036',"yashdeep97@gmail.com"],1)
# 	# user_info_list = obj.get_user_info(1)
# 	#print user_info_list
# 	obj.getUserID()

# if __name__ == '__main__':
#     main()
