# Gates and unlocks

The two moments the run waits on the user's word: a gate note, and the unlock that lets a reviewed fix to a protected harness file land. Read at a gate (SKILL, The run step 5; loop step 12) and when a protected harness change is approved.

## A protected harness change

A reviewed fix to a protected harness file (the hook, the merge script, the check's config) lands through a one-time unlock, in this order. The user says yes in chat. Before writing the note, the lead tells every running implementer not to merge `main` in until it says so, since a branch that merges the base while the note is there gets its own protected changes waved through. The lead writes the note on `main`, quoting the user's yes and the date; applies the reviewed patch on the issue branch (`git am`, since the deny rules lock the implementer out); runs its check and the merge script; deletes the note in the next commit; then lifts the hold.

## Gate note

Post it in chat and as a comment on the gate issue (the issue moves to Needs Review with it, so the comment is what the user sees there). It opens with the ask and the lead's position; the evidence comes after, since a comment that only reports output reads as a review request with nothing to decide.

> **Decision needed from you:** [the one question, in a line]. Reply "go" here or in chat, or name what's wrong.
> **My take:** [the answer the lead recommends], because [the one or two facts that settle it].
> **What "go" unlocks:** the next issues and what they assume.
> **What you'd overrule, if anything:** the closest call or weakest spot, and the cost if it's wrong; "nothing here is close" when that's true.
> Evidence: one line per decision locked, each with the record it implements and where the proof is (a test name, a check line, a file). Rulings made so far that touch it.
> Answers to every question with no objection count as go.
