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
        // NOT working because this. is the object inside array not Tennis1 anymore
        const gameChain = [
            {isGame: this.gameIsTie, score: this.scoreForTie},
            {isGame: this.gameIsAdvantage, score: this.scoreForAdvantage},
            {isGame: this.gameIsOver, score: this.scoreForWinner}]

        for (const game of gameChain) {
            const is_game = game.isGame()
            if (game.isGame()) return game.score()
        }

        return this.scoreForInProgress()
    }

    private scoreForAdvantage() {
        return `Advantage ${this.playerInAdvantage()}`;
    }

    private scoreForInProgress() {
        let tempScore: number = 0;
        let score = ''
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

    private gameIsAdvantage() {
        return (this.m_score1 >= 4 || this.m_score2 >= 4) && (this.scoreDifference() === 1);
    }

    private playerInAdvantage() {
        if (this.m_score1 > this.m_score2) return 'player1'
        if (this.m_score2 > this.m_score1) return 'player2'
        return null
    }

    private scoreDifference() {
        return Math.abs(this.m_score1 - this.m_score2);
    }

    private gameIsOver() {
        return (this.m_score1 >= 4 || this.m_score2 >= 4) && this.scoreDifference() > 1;
    }

    private scoreForTie() {
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

    private gameIsTie() {
        return this.m_score1 === this.m_score2;
    }
}
