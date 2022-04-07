# Kata refactoring

## Simplifying Conditional Logic

- Decompose conditional
  - **Extract function**: `scoreIsTie`
  - **Extract function**: `scoreForTie`
  - **Extract function**: `scoreIsAdvantageOrWin`
  - **Extract function**: `scoreForAdvantageOrWin`
  - **Extract function**: `scoreForInProgress`


- **Replace nested conditional with Guard Clauses**: `getScore`
  - _Temporary field_ smell: `score`
    - **Replace temp with query**: `score`
    - **Change function declaration**: `tieScoreFor`
    - **Change function declaration**: `scoreForInProgress`
  - Finally, remove else branch


## Reveal Intention

- _Mysterious name_ smell or SRP violation: `scoreIsAdvantageOrWin`
  - **Extract function**: `scoreDifference`
  - **Inline variable**: `minusResult`
  - _Duplicated code_ smell: `Advantage` in `playerInAdvantage`
  - **Consolidate conditional expression**: `scoreDifference === 1 or === -1`
  - Change implementation `scoreDifference` with absolute
  - **Replace nested conditional with Guard Clauses**: scoreForAdvantageOrWin


- **Slide statement**: `scoreIsAdvantage` in `getScore`
  - example of fail detected by test (rollback with WebStorm)
  - **Replace nested conditional with Guard Clauses**: `scoreIsAdvantage`


- **Change function declaration**: score --> game
  - `gameIsOver` condition is correct? If I change the function order?
  - Move abs in `scoreDifference`
    - Breaks `scoreForAdvantageOrWin` use `playerinAdvantage` instead
