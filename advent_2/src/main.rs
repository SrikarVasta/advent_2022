use std::str::FromStr;

#[derive(Debug, Clone, Copy)]
enum Move {
    Rock,
    Paper,
    Scissors,
}

#[derive(Debug, Clone, Copy)]
struct Round {
    theirs: Move,
    ours: Move,
}

#[derive(Debug, Clone, Copy)]
enum Outcome {
    Win,
    Draw,
    Loss,
}

impl TryFrom<char> for Move {
    type Error = color_eyre::Report;

    fn try_from(c: char) -> Result<Self, Self::Error> {
        match c {
            'A' | 'X' => Ok(Move::Rock),
            'B' | 'Y' => Ok(Move::Paper),
            'C' | 'Z' => Ok(Move::Scissors),
            _ => Err(color_eyre::eyre::eyre!("not a valid move: {c:?}")),
        }
    }
}

impl FromStr for Round {
    type Err = color_eyre::Report;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut chars = s.chars();
        let (Some(theirs), Some(' '), Some(ours), None) = (chars.next(), chars.next(), chars.next(), chars.next()) else {
            return Err(color_eyre::eyre::eyre!("expected <theirs>SP<ours>EOF, got {s:?}"));
        };

        Ok(Self {
            theirs: theirs.try_into()?,
            ours: ours.try_into()?,
        })
    }
}

impl Move {

    fn inherent_points(self) -> usize {
        match self{
            Move::Rock => 1,
            Move::Scissors => 2,
            Move:: Paper => 3
        }
    }
    
}

impl Move {
    fn beats(self, other:Move) -> bool{
        matches!(
            (self, other),
            (Self::Rock, Self::Paper)
            | (Self::Paper, Self::Rock)
            | (Self::Scissors, Self::Paper)
        )
    }

    fn outcome(self, theirs:Move) -> Outcome {
        if self.beats(theirs){
            Outcome::Win
        } else if theirs.beats(self){
            Outcome::Loss
        } else{
            Outcome::Draw
        }
    }
}

impl Outcome {
    fn inherent_points(self) -> usize {
        match self {
            Outcome::Win => 6,
            Outcome::Draw => 3,
            Outcome::Loss => 0,
        }
    }
}

impl Round {
    fn outcome(self) -> Outcome {
        self.ours.outcome(self.theirs)
    }

    fn our_score(self) -> usize {
        self.ours.inherent_points() + self.outcome().inherent_points()
    }
}

fn main() -> color_eyre::Result<()> {
    color_eyre::install()?;

    for round in include_str!("input.txt")
        .lines()
        .map(|line| line.parse::<Round>())
    {
        let round = round?;
        println!(
            "{round:?}: outcome={outcome:?}, our score={our_score}",
            outcome = round.outcome(),
            our_score = round.our_score()
        );
    }

    Ok(())
}
