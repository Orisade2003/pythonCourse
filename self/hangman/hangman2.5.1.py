HANGMAN_ASCII_ART =  """ 
      Welcome To The Game Hangman
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
MAX_TRIES = 6


def printStates():
    print(r"""picture 1:
    x-------x

picture 2:
    x-------x
    |
    |
    |
    |
    |

picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |

picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |

picture 5:
    x-------x
    |       |
    |       0
    |      /|\
    |
    |

picture 6:
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |

picture 7:
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |""")

def printHangman():
    print(HANGMAN_ASCII_ART)
    print(MAX_TRIES)



if __name__ == '__main__':
    printHangman()
