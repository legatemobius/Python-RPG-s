import random
import time
def enemy_attack2():
    player_health =  player_health - ((enemy_attack - player_defense) + random.randint(-2,5))
def player_attack2():
    enemy_health = enemy_health - ((player_attack - enemy_defense) + random.randint(-2,5))
random1 = random.seed()
action_list = []
enemy_name = "Giant Lizard"
enemy_attack_text = "spits acid at you"
shield_defend = 18
experience = 30
defense_save = 0
enemy_fatigue = 0
player_fatigue = 0
enemy_health = 150 + random.randint(-2,9)
player_max_health = 100
enemy_max_health = enemy_health
enemy_attack = 16 + random.randrange(9)
enemy_defense = 10 + random.randrange(2)
player_health = 70 + random.randrange(10)
player_attack = 8 + random.randint(-2,5)
player_int = 9 + random.randrange(8)
player_defense = 5 + random.randrange(9)
print "            _.===._      ,'^^^^',"
time.sleep(1)
print "           /_\^^^/_\    /  ^ ,^  \      ,"
time.sleep(1)
print "           (0\ ^ /0)\  / ^  /  ^  \    /\   "
time.sleep(1)
print "            \     /  ^^   ^ \ ^ \  ',.' /"
time.sleep(1)
print "             )   (  ^  ^   ^ \   \    ,'"
time.sleep(1)
print "             (o_o)^    \ ^   ,)  /`^^`"
time.sleep(1)
print "              ^V^\ ^ \  \_,-'(((("
time.sleep(1)
print "              /  /`""/  /   "
time.sleep(1)
print "            (((`   '((("
print "you come across a BOSS. you can attack, heal, defend, or run away."
while enemy_health > 0:
    print " "
    print "your turn"
    player_action = raw_input()
    action_list.append(player_action)
    if "attack" in player_action:
            print "you slash at the", enemy_name
            if player_fatigue < 3:
                    player_fatigue = player_fatigue + 0.5
                    if player_attack > enemy_defense:
                            enemy_health = enemy_health - ((player_attack - enemy_defense) + random.randint(-2,5))
                            print "the", enemy_name, enemy_attack_text
                            print "ENEMY health is :", enemy_health
                            player_health =  player_health - ((enemy_attack - player_defense) + random.randint(-2,5))
                            print "YOUR health is :", player_health
                            #normal attack turn.
                    else:
                        #player chip at defenses
                        print "your attack bounces off their armor, denting it."
                        enemy_defense = enemy_defense - 1
                        print "ENEMY health is :", enemy_health
                        print "the", enemy_name, enemy_attack_text
                        player_health =  player_health - (enemy_attack - player_defense)
                        print "YOUR health is", player_health
            else:
                print "your limbs feel like jelly. you try to swing, but collapse on the ground."
                player_health =  player_health - 500
    elif "heal" in player_action or "rest" in player_action:
            #heal
            print "you heal your wounds and"
            print "you feel energized."
            player_health = player_health + player_int + random.randint(-3,9)
            if player_health > player_max_health:
                    player_health = player_max_health
            print "YOUR health is", player_health
            if player_fatigue > 0:
                    if player_fatigue <= 1 and player_fatigue > 0:
                            player_fatigue = 0
                    else:
                        player_fatigue = player_fatigue - 1
            if random.randint(1,4) == 2:
                    print "you are attacked!"
                    player_health =  player_health - ((enemy_attack - player_defense) + random.randint(-2,5))
                    print "ENEMY health is :", enemy_health
                    print "YOUR health is", player_health
                    #heal end
                    #run away script
            else:
                enemy_health = enemy_health + 1
    elif "run away" in player_action:
         break
            #defense script and fatigue
    elif "defend" in player_action:
        if player_fatigue < 3:
            defense_save = player_defense
            player_defense = shield_defend
            player_fatigue = player_fatigue // 1 + 1
            if (enemy_attack - player_defense + random.randint(-5,5)) > 0:

                player_health =  player_health - ((enemy_attack - player_defense) + random.randint(-1,5))
                print "the", enemy_name, enemy_attack_text
                print "YOUR health is", player_health
                player_defense = defense_save
            else:

                print "the", enemy_name, enemy_attack_text
                print "you deflected the blow"
                player_defense = defense_save
                if random.randint(1,2) == 2:
                    print "and you parry!"
                    enemy_health = enemy_health - player_attack - (enemy_defense // 3)
                    print "ENEMY health is", enemy_health
                    print "YOUR health is", player_health
        else:

            print "you are too tired. Heal."
            player_health =  player_health - ((enemy_attack - player_defense) + random.randint(-1,5))
            print "YOUR health is", player_health

    else:
        print "not recognized"
    if player_health < 1:

        print "you died"
        break
    if player_fatigue == 1:

        print "you feel fatigued"
    if player_fatigue == 2:
        print "your limbs ache and breathing is hard"
    if player_fatigue == 3:
        print "Your muscles are burning. you can"
        print "barely breath. HEAL!"
        if enemy_fatigue > 0:
                enemy_fatigue = enemy_fatigue - 0.5
if enemy_health < 1:
    print " "
    print " "
    print "YOU WIN"
    print "you gained", int(enemy_attack + enemy_defense) * 10, "experience"
    experience = experience + (enemy_attack + enemy_defense) * 10
    print "you have", experience, "experience."
else:
  print "YOU LOSE"
print action_list
print "type end"
end = raw_input()
