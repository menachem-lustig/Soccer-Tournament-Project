import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)




def valid_team_name():
    is_valid_string =''
    while not is_valid_string : 
        string = input('Enter a team name: ').strip()
        if string:
            is_valid_string = string
        else:
            logging.warning('The team name can not be empty')
    return is_valid_string



def valid_number(text_for_user,alow_zero =False):
    is_valid_num = False
    num = 0
    while not is_valid_num:
        try:
            num = int(input(text_for_user))
            if not alow_zero:
                if num > 0:
                    is_valid_num = True
                else:
                    logging.warning('The number must to be positive')
            else:
                if num >= 0:
                    is_valid_num = True
                else:
                    logging.warning('The number must to be positive')
        except ValueError:
            logging.warning('The input must to be a number')
    return num



      