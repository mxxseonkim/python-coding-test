def solution(id_pw, db):
    uid, upw = id_pw
    answer = 'fail'
    
    for dbid, dbpw in db:
        if dbid == uid:
            answer = 'login' if dbpw == upw else 'wrong pw'
            break
    
    return answer