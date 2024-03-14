import socketio
import redis
import threading
from datetime import datetime, timedelta

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)
redis_client = redis.Redis(host='localhost', port=6379, db=1)
tokens_to_sid = {}
sid_to_tokens = {}
token_to_league = {}
tokens_in_server = []

def check_queues_for_league_1(data):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("IN CHECK QUEUES FOR LEAGUE 1")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        print("NONE IN QUEUE YET ADDING TO NOOB QUEUE")
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("noob_queue") > 0:
        print("SOMEONE IS IN NOOB QUEUE ADDING TO NOOB QUEUE")
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("bad_queue") > 0:
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("okay_queue") > 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("better_queue") > 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("good_queue") > 0:
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("solid_queue") > 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("super_queue") > 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("mega_queue") > 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("godly_queue") > 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")

def check_queues_for_league_2(data):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("IN CHECK QUEUES FOR LEAGUE 2")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        print("PUSHING USER TO BAD QUEUE 1")
        print("PUSHING USER TO BAD QUEUE 1")
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("bad_queue") > 0:
        print("PUSHING USER TO BAD QUEUE 2")
        print("PUSHING USER TO BAD QUEUE 2")
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        print("PUSHING USER TO NOOB QUEUE")
        print("PUSHING USER TO NOOB QUEUE")
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("okay_queue") > 0:
        print("PUSHING USER TO OKAY QUEUE")
        print("PUSHING USER TO OKAY QUEUE")
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("better_queue") > 0:
        print("PUSHING USER TO BETTER QUEUE")
        print("PUSHING USER TO BETTER QUEUE")
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("good_queue") > 0:
        print("PUSHING USER TO GOOD QUEUE")
        print("PUSHING USER TO GOOD QUEUE")
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("solid_queue") > 0:
        print("PUSHING USER TO SOLID QUEUE")
        print("PUSHING USER TO SOLID QUEUE")
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("super_queue") > 0:
        print("PUSHING USER TO SUPER QUEUE")
        print("PUSHING USER TO SUPER QUEUE")
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("mega_queue") > 0:
        print("PUSHING USER TO MEGA QUEUE")
        print("PUSHING USER TO MEGA QUEUE")
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("godly_queue") > 0:
        print("PUSHING USER TO GODLY QUEUE")
        print("PUSHING USER TO GODLY QUEUE")
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")

def check_queues_for_league_3(data):
    print("############################")
    print("IN CHECK QUEUES FOR LEAGUE 3")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("okay_queue") > 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("bad_queue") > 0:
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("better_queue") > 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("good_queue") > 0:
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("solid_queue") > 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("super_queue") > 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("mega_queue") > 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("godly_queue") > 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")

def check_queues_for_league_4(data):
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("IN CHECK QUEUES FOR LEAGUE 4")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("better_queue") > 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("okay_queue") > 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("bad_queue") > 0:
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("good_queue") > 0:
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("solid_queue") > 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("super_queue") > 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("mega_queue") > 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("godly_queue") > 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")

def check_queues_for_league_5(data):
    print("5555555555555555555555555555")
    print("IN CHECK QUEUES FOR LEAGUE 5")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        print("PUSHING USER TO GOOD QUEUE 1")
        print("PUSHING USER TO GOOD QUEUE 1")
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("good_queue") > 0:
        print("PUSHING USER TO GOOD QUEUE 2")
        print("PUSHING USER TO GOOD QUEUE 2")
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("better_queue") > 0:
        print("PUSHING USER TO BETTER QUEUE")
        print("PUSHING USER TO BETTER QUEUE")
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("okay_queue") > 0:
        print("PUSHING USER TO OKAY QUEUE")
        print("PUSHING USER TO OKAY QUEUE")
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("bad_queue") > 0:
        print("PUSHING USER TO BAD QUEUE")
        print("PUSHING USER TO BAD QUEUE")
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        print("PUSHING USER TO NOOB QUEUE")
        print("PUSHING USER TO NOOB QUEUE")
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("solid_queue") > 0:
        print("PUSHING USER TO SOLID QUEUE")
        print("PUSHING USER TO SOLID QUEUE")
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("super_queue") > 0:
        print("PUSHING USER TO SUPER QUEUE")
        print("PUSHING USER TO SUPER QUEUE")
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("mega_queue") > 0:
        print("PUSHING USER TO MEGA QUEUE")
        print("PUSHING USER TO MEGA QUEUE")
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("godly_queue") > 0:
        print("PUSHING USER TO GODLY QUEUE")
        print("PUSHING USER TO GODLY QUEUE")
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")
     
def check_queues_for_league_6(data):
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("IN CHECK QUEUES FOR LEAGUE 6")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("solid_queue") > 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("good_queue") > 0:
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("better_queue") > 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("okay_queue") > 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("bad_queue") > 0:
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("super_queue") > 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("mega_queue") > 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("godly_queue") > 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")
  
def check_queues_for_league_7(data):
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("IN CHECK QUEUES FOR LEAGUE 7")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("super_queue") > 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("solid_queue") > 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("good_queue") > 0:
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("better_queue") > 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("okay_queue") > 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("bad_queue") > 0:
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("mega_queue") > 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("godly_queue") > 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")
  
def check_queues_for_league_8(data):
    print("****************************")
    print("IN CHECK QUEUES FOR LEAGUE 8")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("mega_queue") > 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("super_queue") > 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("solid_queue") > 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("good_queue") > 0:
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("better_queue") > 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("okay_queue") > 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("bad_queue") > 0:
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")
    elif get_length_of_queue("godly_queue") > 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")

def check_queues_for_league_9(data):
    print("(((((((((((((())))))))))))))")
    print("IN CHECK QUEUES FOR LEAGUE 9")
    TOKEN = data.split("|")[0]
    print(f"TOKEN: {TOKEN}")
    SID = data.split("|")[1]
    print(f"SID: {SID}")
    if get_length_of_all_queues() == 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
    elif get_length_of_queue("godly_queue") > 0:
        redis_client.rpush('godly_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("godly_queue")
        match_players(q_length, "godly_queue")
    elif get_length_of_queue("mega_queue") > 0:
        redis_client.rpush('mega_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("mega_queue")
        match_players(q_length, "mega_queue")
    elif get_length_of_queue("super_queue") > 0:
        redis_client.rpush('super_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("super_queue")
        match_players(q_length, "super_queue")
    elif get_length_of_queue("solid_queue") > 0:
        redis_client.rpush('solid_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("solid_queue")
        match_players(q_length, "solid_queue")
    elif get_length_of_queue("good_queue") > 0:
        redis_client.rpush('good_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("good_queue")
        match_players(q_length, "good_queue")
    elif get_length_of_queue("better_queue") > 0:
        redis_client.rpush('better_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("better_queue")
        match_players(q_length, "better_queue")
    elif get_length_of_queue("okay_queue") > 0:
        redis_client.rpush('okay_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("okay_queue")
        match_players(q_length, "okay_queue")
    elif get_length_of_queue("bad_queue") > 0:
        redis_client.rpush('bad_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("bad_queue")
        match_players(q_length, "bad_queue")
    elif get_length_of_queue("noob_queue") > 0:
        redis_client.rpush('noob_queue', data)
        tokens_to_sid[TOKEN] = SID
        sid_to_tokens[SID] = TOKEN
        token_to_league[TOKEN] = 10
        overall_queue_length = get_length_of_all_queues()
        sio.emit('PUTINQUEUE', f"SUCCESS|{overall_queue_length - 1}", room=SID)
        q_length = get_length_of_queue("noob_queue")
        match_players(q_length, "noob_queue")

def push_user_into_queue(data, league):
    if league == 1:
        check_queues_for_league_1(data)
    elif league == 2:
        check_queues_for_league_2(data)
    elif league == 3:
        check_queues_for_league_3(data)
    elif league == 4:
        check_queues_for_league_4(data)
    elif league == 5:
        check_queues_for_league_5(data)
    elif league == 6:
        check_queues_for_league_6(data)
    elif league == 7:
        check_queues_for_league_7(data)
    elif league == 8:
        check_queues_for_league_8(data)
    elif league == 9:
        check_queues_for_league_9(data)
    overall_length = get_length_of_all_queues()
    sio.emit("CHECKQUEUE", f"Length|{overall_length}")

def get_league_from_string(league_name):
    if league_name == "noob_queue":
        return 1
    elif league_name == "bad_queue":
        return 2
    elif league_name == "okay_queue":
        return 3
    elif league_name == "better_queue":
        return 4
    elif league_name == "good_queue":
        return 5
    elif league_name == "solid_queue":
        return 6
    elif league_name == "super_queue":
        return 7
    elif league_name == "mega_queue":
        return 8
    elif league_name == "godly_queue":
        return 9

def match_players(queue_len, queue_name):
    print("IN MATCH PLAYERS FUNCTION")
    # set boolean so if check_queue is called but currently matching players 
    # then dont match players; might cause overlap
    # maybe check_queue for each individual queue so other queues can check
    # without overlap
    invalid_user = False
    invalid_token1 = ""
    invalid_sid1 = ""
    invalid_token2 = ""
    invalid_sid2 = ""
    if queue_len > 1:
        print("QUEUE LENGTH IS GREATER THAN 1")
        while True:
            player_1_bytes = redis_client.lpop(queue_name)
            player_1_string = player_1_bytes.decode()
            player_1 = player_1_string.split("|")[0]
            player_1_sid = player_1_string.split("|")[1]
            player_2_bytes = redis_client.lpop(queue_name)
            player_2_string = player_2_bytes.decode()
            player_2 = player_2_string.split("|")[0]
            player_2_sid = player_2_string.split("|")[1]
            if player_1 == player_2:
                invalid_user = True
                invalid_token1 = player_1
                invalid_sid1 = player_1_sid
                invalid_token2 = player_2
                invalid_sid2 = player_2_sid
                break
            MESSAGE = player_1 + "|" + player_2
            print(f"MESSAGE: {MESSAGE}")
            sio.emit("FOUNDGAME1", MESSAGE, room=player_1_sid)
            new_queue_len = get_length_of_queue(queue_name)
            print(f"NEW QUEUE LENGTH: {new_queue_len}")
            if new_queue_len <= 1:
                print("BREAKING FROM MATCH PLAYERS")
                break
        if invalid_user:
            league_num = get_league_from_string(queue_name)
            remove_user_from_server(invalid_token1, invalid_sid1, league_num)
            remove_user_from_server(invalid_token2, invalid_sid2, league_num)
        overall_length = get_length_of_all_queues()
        sio.emit("CHECKQUEUE", f"Length|{overall_length}")

def get_length_of_queue(queue_name):
    queue_contents = redis_client.lrange(queue_name, 0, -1)
    queue_length = len(queue_contents)
    return queue_length

def get_length_of_all_queues():
    noob_q_length = get_length_of_queue("noob_queue")
    bad_q_length = get_length_of_queue("bad_queue")
    okay_q_length = get_length_of_queue("okay_queue")
    better_q_length = get_length_of_queue("better_queue")
    good_q_length = get_length_of_queue("good_queue")
    solid_q_length = get_length_of_queue("solid_queue")
    super_q_length = get_length_of_queue("super_queue")
    mega_q_length = get_length_of_queue("mega_queue")
    godly_q_length = get_length_of_queue("godly_queue")
    overall_queue_length = noob_q_length + bad_q_length + okay_q_length + better_q_length + good_q_length + solid_q_length + super_q_length + mega_q_length + godly_q_length
    return overall_queue_length

def remove_user_from_server(token, sid, LEAGUE):
    print("IN REMOVE USER FROM SERVER")
    print(f"TOKEN: {token}")
    print(f"SID: {sid}")
    print(f"LEAGUE: {LEAGUE}")
    league = int(LEAGUE)
    tokens_in_server.remove(token)
    if league == 1:
        queue_contents = redis_client.lrange('noob_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('noob_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 2:
        queue_contents = redis_client.lrange('bad_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('bad_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 3:
        queue_contents = redis_client.lrange('okay_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('okay_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 4:
        queue_contents = redis_client.lrange('better_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('better_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 5:
        queue_contents = redis_client.lrange('good_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('good_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 6:
        queue_contents = redis_client.lrange('solid_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('solid_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 7:
        queue_contents = redis_client.lrange('super_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('super_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 8:
        queue_contents = redis_client.lrange('mega_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('mega_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")
    elif league == 9:
        queue_contents = redis_client.lrange('godly_queue', 0, -1)
        for u in queue_contents:
            user = u.decode()
            if user.split("|")[1] == sid:
                print("IT IS A MATCH DISONNECT USER")
                redis_client.lrem('godly_queue', 0, user)
        try:
            del tokens_to_sid[token]
            del sid_to_tokens[sid]
            del token_to_league[token]
        except:
            print("ALREADY REMOVED USER INFO")

@sio.event
def connect(sid, environ):
    print('Client connected', sid)
    # sio.emit("connected", "Hello World", room=sid)

@sio.event
def put_in_queue(sid, data):
    data_split = data.split("|")
    TOKEN = data_split[0]
    print(f"TOKEN: {TOKEN}")
    print(f"TOKENS IN SERVER: {tokens_in_server}")
    if TOKEN not in tokens_in_server:
        tokens_in_server.append(TOKEN)
        LEAGUE = data_split[1] 
        print(f"LEAGUE: {LEAGUE}")
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S")
        input_data = TOKEN + "|" + sid + "|" + formatted_time
        print(f"Input Data: {input_data}")
        noob_q_length = get_length_of_queue("noob_queue")
        print(f"noob_q_length: {noob_q_length}")
        bad_q_length = get_length_of_queue("bad_queue")
        print(f"bad_q_length: {bad_q_length}")
        okay_q_length = get_length_of_queue("okay_queue")
        print(f"okay_q_length: {okay_q_length}")
        better_q_length = get_length_of_queue("better_queue")
        print(f"better_q_length: {better_q_length}")
        good_q_length = get_length_of_queue("good_queue")
        print(f"good_q_length: {good_q_length}")
        solid_q_length = get_length_of_queue("solid_queue")
        print(f"solid_q_length: {solid_q_length}")
        super_q_length = get_length_of_queue("super_queue")
        print(f"super_q_length: {super_q_length}")
        mega_q_length = get_length_of_queue("mega_queue")
        print(f"mega_q_length: {mega_q_length}")
        godly_q_length = get_length_of_queue("godly_queue")
        print(f"godly_q_length: {godly_q_length}")
        push_user_into_queue(input_data, int(LEAGUE))

@sio.event
def created_game(sid, data):
    data_split = data.split("|")
    SENDING_TOKEN = data_split[0]
    PLAYER_1 = data_split[1]
    PLAYER_2 = data_split[2]
    GAME_ID = data_split[3]
    sending_user_sid = tokens_to_sid[SENDING_TOKEN]
    MESSAGE = PLAYER_1 + "|" + PLAYER_2 + "|" + GAME_ID
    sio.emit("CREATEDGAME", MESSAGE, room=sending_user_sid)

@sio.event
def remove_from_server(sid, data):
    try:
        data_split = data.split("|")
        PLAYER_1_TOKEN = data_split[0]
        PLAYER_2_TOKEN = data_split[1]
        PLAYER_1_SID = tokens_to_sid[PLAYER_1_TOKEN]
        PLAYER_2_SID = tokens_to_sid[PLAYER_2_TOKEN]
        del tokens_to_sid[PLAYER_1_TOKEN]
        del tokens_to_sid[PLAYER_2_TOKEN]
        del sid_to_tokens[PLAYER_1_SID]
        del sid_to_tokens[PLAYER_2_SID]
        del token_to_league[PLAYER_1_TOKEN]
        del token_to_league[PLAYER_2_TOKEN]
        tokens_in_server.remove(PLAYER_1_TOKEN)
        tokens_in_server.remove(PLAYER_2_TOKEN)
        sio.emit("LEFTSERVER", room=PLAYER_1_SID)
        sio.emit("LEFTSERVER", room=PLAYER_2_SID)
    except:
        print("ALREADY REMOVED USERS")

@sio.event
def disconnect(sid):
    print('Client disconnected', sid)
    try:
        TOKEN = sid_to_tokens[sid]
        LEAGUE = token_to_league[TOKEN]
        # Send message to all users updating
        # the length of the queue
        remove_user_from_server(TOKEN, sid, LEAGUE)
    except:
        print("ALREADY REMOVED USER")

@sio.event
def message(sid, data):
    print('Message from client:', data)

if __name__ == '__main__':
    import eventlet
    eventlet.wsgi.server(eventlet.listen(('localhost', 8765)), app)