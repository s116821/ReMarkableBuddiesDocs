# Maintained input serialization

The pinned octokit/request-action source `b91aabaa...` calls YAML.load on every
INPUT value. GitHub must pass `toJSON(steps.complete.outputs.notes)`: a JSON string
is a valid YAML scalar, and the maintained parser returns the original text.
No quoting, newline replacement or ad-hoc YAML serializer is introduced.

The focused actual-Action fixture uses a loopback API, multiline version/source
and completion-marker text including colons/quotes/Unicode. The unencoded input
must fail before PATCH; the encoded input must produce exactly the original JSON
body string. Assert the production workflow uses the same expression. Preserve
the observed failure and distinguish owned fixture evidence from production.

The existing main attempt is immutable. Its matching uploaded draft is not called
published, and no rerun is claimed to load this successor workflow. Root owns any
explicit recovery decision with original source/artifact/draft identity intact.
New source repair PRs start at Buddy1d1b480d, Manager959205e7 and Docs9fe07b46;
old source branches and all original run evidence remain untouched.
