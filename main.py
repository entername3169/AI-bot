import discord
from discord.ext import commands
from classification import get_class
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'hi nigg-')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def img(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            filename = attachment.filename
            img_path = f"img/{filename}"
            await attachment.save(img_path)

        class_name, score = get_class("keras_model.h5", "labels.txt", img_path)
        await ctx.send(f"this a {class_name.strip()} frfr")
        if class_name.strip() == "kat":
            await ctx.send('''ok here is some info about cats:
            Cats are small, carnivorous mammals that are often kept as pets. Here is some information about cats:

            Scientific Classification:

            Kingdom: Animalia
            Phylum: Chordata
            Class: Mammalia
            Order: Carnivora
            Family: Felidae
            Genus: Felis
            Species: Various species, including Felis catus (domestic cat)
            Domestication:

            Cats are one of the oldest domesticated animals, and they have been living with humans for thousands of years.
            Domestic cats are valued by humans for companionship and their ability to control pests, such as rodents.
            Physical Characteristics:

            Cats come in various breeds, each with its own unique characteristics.
            They have retractable claws and keen senses, including excellent night vision and a well-developed sense of smell.
            Their whiskers are highly sensitive and help them navigate in the dark.
            Behavior:

            Cats are known for their grooming behavior, spending a significant amount of time cleaning their fur.
            They are often playful and may engage in activities like chasing toys or hunting imaginary prey.
            Cats are territorial animals, and they may mark their territory by rubbing scent glands located on their face against objects.

            Cats are beloved pets around the world, and their diverse personalities and behaviors make them fascinating companions.''')
        elif class_name.strip() == "doug":
            await ctx.send('''
                        
            Certainly! Dogs are one of the most popular and diverse species of domesticated animals, known for their companionship, loyalty, and various roles in human society. Here's some information about dogs:

            Scientific Classification:

            Kingdom: Animalia
            Phylum: Chordata
            Class: Mammalia
            Order: Carnivora
            Family: Canidae
            Genus: Canis
            Species: Various species, including Canis lupus familiaris (domestic dog)
            Domestication:

            Dogs were one of the first animals to be domesticated by humans, with a history dating back thousands of years.
            They were initially domesticated for various purposes, including hunting, herding, guarding, and companionship.
            Physical Characteristics:

            Dogs exhibit a wide range of sizes, shapes, and coat types due to the vast number of breeds.
            They have a strong sense of smell, excellent hearing, and, in many cases, a keen sense of sight.
            Dogs have a remarkable ability to understand and respond to human gestures and vocal cues.

            Dogs have played a significant role in human history and continue to be cherished members of families worldwide. Their versatility, intelligence, and loyalty make them valued companions in a variety of roles.


            ''')
    else:
        await ctx.send("ni@!# this sh#! is empty send an image or somethin like nah bro what the hell?")



bot.run("MTEyODM2Mzg2ODg2ODA1OTE5Ng.G7XZmA.dr7EsTt8jQHqfWNx71BVfIgAb5XBtcC_96mt8M")