import {TennisGame} from './TennisGame';
import {AdvantageScore, EndScore, InProgressScore, TieScore} from "./Score";

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
        const inProgressScore = new InProgressScore(this.m_score1, this.m_score2)
        const tieScore = new TieScore(this.m_score1, this.m_score2)
        const advantageScore = new AdvantageScore(this.m_score1, this.m_score2)
        const gameOverScore = new EndScore(this.m_score1, this.m_score2)

        const possibleScores = [inProgressScore, tieScore, advantageScore, gameOverScore]

        const currentScore = possibleScores.filter((s) => s.isCurrentScore())[0]
        return currentScore.render()

        throw new Error('What game are you playing?')
    }
}
