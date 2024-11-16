from objectionpy import preset, enums, assets, objection
from objectionpy.frames import *

scene = objection.Scene()

def frameWithCharacterPose(characterChosen, whatTheySay, pose, bubbleChosen):
    scene.frames.append(Frame(
    char = FrameCharacter(
        character=characterChosen,
        poseSubstr=pose
    ),
    text = whatTheySay,
    bubble = bubbleChosen
))

# PASTE THE CHATGPT OUTPUT UNDER HERE 
frameWithCharacterPose(preset.Characters.Judge().TheJudge, f"{preset.Music().Trial} Court is now in session for the trial of the Top 20 True and the Rainbow Kingdom & Gabby's Dollhouse Characters.", "Stand", 2) 

frameWithCharacterPose(preset.Characters.Defense().PhoenixWright, f"{preset.Music().Moderato2009} Your Honor, the defense is ready to prove the significance of the accused characters in their respective shows.", "Confident", None)

frameWithCharacterPose(preset.Characters.Prosecution().MilesEdgeworth, f"{preset.Music().Cornered2009} The prosecution intends to demonstrate the lack of value these characters bring to their narratives.", "Confident Smirk", None)

frameWithCharacterPose(preset.Characters.Defense().ApolloJustice, "Objection! These characters have impacted countless fans with their relatable personalities and memorable moments.", "Point", 1)

frameWithCharacterPose(preset.Characters.Prosecution().FranziskaVonKarma, "Hold it! Impact is subjective. The question is whether they serve a meaningful purpose in their stories.", "Whip Desk", 2)

frameWithCharacterPose(preset.Characters.Witness().LarryButz, f"{preset.Music().Gumshoe} Uh... I'm not sure what I'm doing here, but I think Gabby has cute cat ears, so that counts, right?", "Nervous", None)

frameWithCharacterPose(preset.Characters.Defense().PhoenixWright, "Hold it! Larry, focus! How do you feel these characters enhance the narratives?", "Thinking", 2)

frameWithCharacterPose(preset.Characters.Witness().LarryButz, "Oh, uh... They inspire hope and creativity for kids! That's important!", "Thumbs Up", None)

frameWithCharacterPose(preset.Characters.Prosecution().MilesEdgeworth, "And yet, inspiration alone does not justify relevance. We require proof of their narrative contributions.", "Point", 2)

frameWithCharacterPose(preset.Characters.Defense().ApolloJustice, f"{preset.Music().Cornered2007Variation} Here is the evidence, Your Honor! The characters embody themes of kindness, teamwork, and resilience.", "Desk slam", 3)

frameWithCharacterPose(preset.Characters.Judge().TheJudge, "Hmm... I must admit, those themes are essential for any impactful story.", "Positive", None)

frameWithCharacterPose(preset.Characters.Prosecution().Godot, "Take that! But what about the redundancy among these characters? Surely not all 20 are unique.", "Desk Slam (with mug)", 3)

frameWithCharacterPose(preset.Characters.Defense().PhoenixWright, "Objection! Each character contributes distinct qualities, from True’s problem-solving to Gabby's nurturing creativity.", "Point", 1)

frameWithCharacterPose(preset.Characters.Judge().TheJudge, f"{preset.Music().Truth2007} I believe I have heard enough. Both sides have presented compelling arguments. I will now deliberate on this matter.", "Headshake", None) 

frameWithCharacterPose(preset.Characters.Judge().TheJudge, "Court is adjourned.", "Stand", 2)







with open('./scene.objection', 'w') as f:
    f.write(scene.makeObjectionFile(scene.compile()))
