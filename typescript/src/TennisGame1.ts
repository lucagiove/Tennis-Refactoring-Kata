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
        if (!this.playerInAdvantage())
            return this.tieScoreNameFor(this.player1Score);

        if (this.gameIsAdvantage())
            return `Advantage ${this.playerInAdvantage()}`;

        if (this.gameIsOver())
                return `Win for ${this.playerInAdvantage()}`;

        return `${this.scoreNameFor(this.player1Score)}-${this.scoreNameFor(this.player2Score)}`

    }

    private gameIsAdvantage() {
        return (this.scoreDifference() === 1) && (this.player1Score >= 4 || this.player2Score >= 4) ;
    }

    private gameIsOver() {
        return (this.scoreDifference() >= 2) && (this.player1Score >= 4 || this.player2Score >= 4) ;
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

    private scoreNameFor(score: number) {
        switch (score) {
            case 0:
                return 'Love';
            case 1:
                return 'Fifteen';
            case 2:
                return 'Thirty';
            case 3:
                return'Forty';
            default:
                throw new Error("Score name unknown")
        }
    }

    private tieScoreNameFor(score: number) {
        let result: string
        switch (score) {
            case 0:
                result = 'Love-All';
                break;
            case 1:
                result = 'Fifteen-All';
                break;
            case 2:
                result = 'Thirty-All';
                break;
            default:
                result = 'Deuce';
                break;

        }
        return result;
    }
}
