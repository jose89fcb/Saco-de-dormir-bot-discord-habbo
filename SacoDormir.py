import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
import random


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def saco(ctx,   keko):
    await ctx.message.delete()
    await ctx.send("Generando saco de dormir...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko}")
 
   
    
    habbo = response.json()['figureString']
  
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=m&figure="+ habbo +"&action=none&direction=2&head_direction=2&gesture=std&size=m&headonly=1"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((54,62), Image.Resampling.LANCZOS)#tamaño del keko 1

   
    
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    ###

    


    saco = Image.open(r"imagenes/saco.png").convert("RGBA") #imagen
    img1 = saco.resize((88,103), Image.Resampling.LANCZOS)#tamaño de la saco


    ###
  
    ###
    

    
    

 
   
    
    
    
    
    
    
    
  
    img1.paste(saco,(0,0), mask = saco) #Posicion de la saco
    img1.paste(img2,(15,-12), mask = img2) #Posicion del keko 1
    
    
  

    
    ### 

    
    
   
    
   ###
   
    
   
    ###
    
   
 
    
    
  ####
   
  ###
    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   