abstract class Score {
    protected constructor(protected m_score1: number, protected m_score2: number) {
    }

    public isCurrentScore(): boolean {
        throw new Error('Not Implemented')
    }

    public render(): string {
        throw new Error('Not Implemented')
    }

    protected scoreDifference() {
        return this.m_score1 - this.m_score2;
    }

    protected playerInAdvantage() {
        if (this.m_score1 > this.m_score2)
            return "player1"
        if (this.m_score2 > this.m_score1)
            return "player2"
        return null
    }
}

export class InProgressScore extends Score {
    constructor(m_score1: number, m_score2: number) {
        super(m_score1, m_score2);
    }

    public isCurrentScore(): boolean {
        return (this.m_score1 !== this.m_score2) && (this.m_score1 < 4 && this.m_score2 < 4);
    }

    public render(): string {
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
}

export class TieScore extends Score {
    constructor(m_score1: number, m_score2: number) {
        super(m_score1, m_score2);
    }

    public isCurrentScore(): boolean {
        return this.m_score1 === this.m_score2;
    }

    public render(): string {
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

export class AdvantageScore extends Score {
    constructor(m_score1: number, m_score2: number) {
        super(m_score1, m_score2);
    }

    public isCurrentScore(): boolean {
        return (this.m_score1 >= 4 || this.m_score2 >= 4) && (Math.abs(this.scoreDifference()) === 1);
    }

    public render(): string {
        return `Advantage ${this.playerInAdvantage()}`;

    }
}

export class EndScore extends Score {
    constructor(m_score1: number, m_score2: number) {
        super(m_score1, m_score2);
    }

    public isCurrentScore(): boolean {
        return (this.m_score1 >= 4 || this.m_score2 >= 4) && (Math.abs(this.scoreDifference()) > 1);
    }

    public render(): string {
        if (this.scoreDifference() >= 2) return 'Win for player1';
        return 'Win for player2';
    }

}
