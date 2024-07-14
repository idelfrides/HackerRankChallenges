
from challenges.adatech import ada_challenges
from LIBS import manager as man
from challenges import grid_challenge


# ---------------------------------------------------------------


def run_challenge():
  ada_challenges.run_ada_challenges()
  return

def make_some_tests():
  man.some_personal_verifications()
  return

def run_grid_challenge():
  # grid_challenge.run_grid_challenge_via_terminal()
  grid_challenge.run_grid_challenge_through_files()


if __name__ == "__main__":
  run_grid_challenge()
  # make_some_tests()
  # run_challenge()
  