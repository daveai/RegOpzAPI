from flask import Flask, jsonify, request
from flask_restful import Resource
from Helpers.authenticate import *
from Constants.Status import *
from Models.RegOpzUser import RegOpzUser
import json
class UserController(Resource):	
	def get(self, userId=None):
		if userId:	  
			regOpzUser = RegOpzUser()  	
			res = regOpzUser.get(userId)
			return res
		return RegOpzUser().get()
	def post(self):
		auth = request.authorization        
		if auth:
			#it is login called
			return RegOpzUser().login(auth['username'],auth['password'])
		user = request.get_json(force=True)		
		regOpzUser = RegOpzUser(user)
		res = regOpzUser.save()
		return res
	
