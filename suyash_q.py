from aditya import *
from suyash import *
from tushar import *
def suy(ch, con, cur):
    if(ch==5):
        query_5(con,cur)


def query_5(con, cur):
    team1 = input("Enter First Team:")
    team2 = input("Enter Second Team")
    stadium = input("Enter the first phone number of the stadium")
    ref = input("Enter referee ID")
    dat=input("Enter date of the match")
    if(1 or (not check_name(team1) and  not check_name(team2) and  not check_number(stadium) and  not ref.isnumeric() and not datecheck(dat))):
        query = f"INSERT INTO futsal_match(match_date, sfpn) VALUES({dat}, {stadium});"
        try:
            cur.execute(query)
        except Exception as e:
            print(e)
        print(query)
        con.commit()
        query = f"SELECT AUTO_INCREMENT FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'futsal' AND   TABLE_NAME   = 'futsal_match';"
        id=cur.lastrowid
        print("ID ISSSS", id)
        query = f"INSERT INTO team_match(team_name, match_id) VALUES({team1}, {id});"
        print(query)
        try:
            cur.execute(query)
        except Exception as e:
            print(e)
        con.commit()
        query = f"INSERT INTO team_match(team_name, match_id) VALUES({team2}, {id});"
        print(query)
        try:
            cur.execute(query)
        except Exception as e:
            print(e)
        con.commit()
        query = f"INSERT INTO referee_match(referee_id, match_id) VALUES({ref}, {id});"
        print(query)
        try:
            cur.execute(query)
        except Exception as e:
            print(e)
        con.commit()
        query=f"select jersey_no from player where team_name={team1};"
        cur.execute(query)
        for row in cur:
            query2=f"INSERT INTO player_match(pjn, match_id, team_name) VALUES({int(row['jersey_no'])}, {id}, {team1});"
            cur.execute(query2)
            con.commit()
        query=f"select jersey_no from player where team_name={team2};"
        cur.execute(query)
        for row in cur:
            query2=f"INSERT INTO player_match(pjn, match_id, team_name) VALUES({int(row['jersey_no'])}, {id}, {team2});"
            cur.execute(query2)
            con.commit()
        stadium_increment(stadium)
        referee_increment(ref)

    else:
        return 1
    print(query)
    con.commit()

    print("Inserted into database")

def query_9(con, cur):
    first_name=input("Enter first name")
    middle_name=input("Enter middle name")
    last_name=input("Enter last name")
    team_name = input("Enter the Team of the coach to be replaced")
    experience=int(input("Enter experience of the coach"))
    gender=input("Enter M or F")
    query = f"UPDATE coach SET experience = '{experience}', gender='{gender}' WHERE team_name='{team_name}';"
    try:
        curr.execute(query)
        con.commit()
    except:
        print("The Team does not exist.")
        return
    query = f"UPDATE coach_name SET first_name='{first_name}', middle_name='{middle_name}', last_name='{last_name}' WHERE team_name='{team_name}';"
    try:
        curr.execute(query)
        con.commit()
    except:
        print("The Team does not exist.")
        return

def query_14(con, cur):
    team_name=input("Enter team name")
    jersey=int(input("Enter jersey number"))
    match_id=int(input("Enter match ID"))
    spn=input("Enter stadium's first phone number")
    query1=f"SELECT EXISTS(SELECT * FROM goals_scored WHERE pjn='{jersey}' AND team_name='{team_name}' AND match_id='{match_id}' ;);"
    try:
        val=curr.execute(query1)
        print(val)
        if val==0:
            query=f"INSERT INTO goal_scored(pjn, team_name, match_id, nog) VALUES ({jersey}, {team_name}, {match_id}, 1);"
        else:
            query = f"UPDATE goal_scored SET nog = nog + 1 WHERE pjn='{jersey}' AND team_name='{team_name}' AND match_id='{match_id}' ;"
        curr.execute(query)
        con.commit()
    except:
        print("Invalid details")

def query_21(con, cur):
    team_name=input("Enter team name")
    query = f"SELECT * from team WHERE name={team_name};"
    cur.execute(query)
    table = list()
    table.append(["team name","wins","losses", "draw"])
    for row in cur:
        table.append([row['name'], row['wins'], row['losses'], row['draw']])
    print_table(table)

def query_22(con, cur):
    match_id = input("Enter match ID: ")
    try:
        match_id = int(match_id)
    except ValueError:
        print("You have to enter integer")
        return
    query1=f"SELECT team_name from team_match WHERE match_id={match_id};"
    cur.execute(query1)
    i=0
    for row in cur:
        if i==0:
            team1=row['team_name']
        else:
            team2=row['team_name']
        i=i+1
    query = f"SELECT * from futsal_match WHERE match_id={match_id};"
    cur.execute(query)
    table = list()
    table.append(["Match_id","Date","Total Goals", "Winner", "Loser", "Stadium"])
    for row in cur:
        if(team1==row['winner_id']):
            loser=team2
        else:
            loser=team1
        query=f"SELECT building_name FROM stadium WHERE fpn={row['sfpn']};"
        cur.execute(query)
        for row in cur:
            stadname=row['building_name']
        print(row['match_id'], row['match_date'], row['winner_id'], loser, row['total_goals'], stadname)
    print_table(table)
