import {TennisGame} from './TennisGame';


export class TennisGame1 implements TennisGame {
    private player1Score: number = 0;
    private player2Score: number = 0;
    private player1Name: string;
    private player2Name: string;

    constructor(player1Name: string, player2Name: string) {
        this.player1Name = player1Name;
        this.player2Name = player2Name;
    }

    wonPoint(playerName: string): void {
        if (playerName === 'player1')
            this.player1Score += 1;
        else
            this.player2Score += 1;
    }

    getScore(): string {

        if (this.gameIsOver())
            return `Win for ${this.playerInAdvantage()}`;


        if (this.gameIsAdvantage())
            return `Advantage ${this.playerInAdvantage()}`;


        if (this.gameInProgress())
            return `${TennisGame1.scoreNameFor(this.player1Score)}-${TennisGame1.scoreNameFor(this.player2Score)}`


        if (this.gameIsTie())
            return TennisGame1.tieScoreNameFor(this.player1Score);

    }

    private gameInProgress() {
        return !(this.gameIsTie() || this.gameIsAdvantage() || this.gameIsOver());
    }

    private gameIsTie() {
        return !this.playerInAdvantage();
    }

    private gameIsAdvantage() {
        return (this.scoreDifference() === 1) && (this.player1Score >= 4 || this.player2Score >= 4);
    }

    private gameIsOver() {
        return (this.scoreDifference() >= 2) && (this.player1Score >= 4 || this.player2Score >= 4);
    }

    private scoreDifference() {
        return Math.abs((this.player1Score - this.player2Score));
    }

    private playerInAdvantage(): string | null {
        if (this.player1Score > this.player2Score)
            return this.player1Name
        if (this.player1Score < this.player2Score)
            return this.player2Name
        return null
    }

    private static scoreNameFor(score: number) {
        switch (score) {
            case 0:
                return 'Love';
            case 1:
                return 'Fifteen';
            case 2:
                return 'Thirty';
            case 3:
                return 'Forty';
            default:
                throw new Error(`Score name unknown for: ${score}`)
        }
    }

    private static tieScoreNameFor(score: number) {
        if(score > 2)
            return "Deuce"
        return `${TennisGame1.scoreNameFor(score)}-All`;
    }
}
