class Player:
  def getVersion ():
    """
    Returns the current version of the deployed bot.
    Useful to get debug information.
    """
    return "Default py-player"

  def bet (self, gamestate):
    """
    Returns the amount for the next bet.
    Return 0 to fold.
    """
    print "Playing game {0}".format(gamestate["tournamentId"])

    # Fold every single hand
    return 0
