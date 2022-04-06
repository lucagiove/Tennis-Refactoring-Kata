import {TennisGame} from './TennisGame';


export class TennisGame1 implements TennisGame {
    private m_score1: number = 0;
    private m_score2: number = 0;
    private player1Name: string;
    private player2Name: string;

    constructor(player1Name: string, player2Name: string) {
        this.player1Name = player1Name;
        this.player2Name = player2Name;
    }

    wonPoint(playerName: string): void {
        if (playerName === 'player1')
            this.m_score1 += 1;
        else
            this.m_score2 += 1;
    }

    getScore(): string {

        if (this.gameIsInProgress()) {
            return this.scoreForInProgress();
        }

        if (this.gameIsPair()) {
            return this.tieScoreFor()
        }

        if (this.gameIsAdvantage()) {
            return this.scoreForAdvantage();
        }

        if (this.gameIsOver()) {
            return this.scoreForWinner();
        }
    }

    private gameIsInProgress() {
        return !(this.gameIsPair() || this.gameIsAdvantage() || this.gameIsOver())
    }

    private gameIsPair() {
        return this.m_score1 === this.m_score2;
    }

    private gameIsAdvantage() {
        return (this.m_score1 >= 4 || this.m_score2 >= 4) && this.scoreDifference() === 1
    }

    private gameIsOver() {
        return (this.m_score1 >= 4 || this.m_score2 >= 4) && this.scoreDifference() > 1;
    }

    private scoreForAdvantage() {
        return `Advantage ${this.playerInAdvantage()}`;
    }

    private scoreForInProgress() {
        let score = ''
        let tempScore: number = 0;
        for (let i = 1; i < 3; i++) {
            if (i === 1) tempScore = this.m_score1;
            else {
                score += '-';
                tempScore = this.m_score2;
            }
            switch (tempScore) {
                case 0:
                    score += 'Love';
                    break;
                case 1:
                    score += 'Fifteen';
                    break;
                case 2:
                    score += 'Thirty';
                    break;
                case 3:
                    score += 'Forty';
                    break;
            }
        }
        return score;
    }

    private scoreForWinner() {
        return `Win for ${this.playerInAdvantage()}`;
    }

    private playerInAdvantage() {
        if (this.m_score1 > this.m_score2)
            return 'player1'
        if (this.m_score2 > this.m_score1)
            return 'player2'
        return null
    }

    private scoreDifference() {
        return Math.abs(this.m_score1 - this.m_score2);
    }

    private  tieScoreFor() {
        switch (this.m_score1) {
            case 0:
                return 'Love-All';
            case 1:
                return 'Fifteen-All';
            case 2:
                return 'Thirty-All';
            default:
                return 'Deuce';
        }
    }

}
