.PHONY: test validate-rubric validate-example validate-submission release-check

test:
	python3 -m unittest discover -s tests -v

validate-rubric:
	python3 scripts/validate_rubric.py

validate-example:
	python3 scripts/validate_submission.py examples/b2b-supportpilot-example.md

validate-submission:
	@test -n "$(FILE)" || (echo "Usage: make validate-submission FILE=submissions/<student-id>/operating-dashboard.md" && exit 2)
	python3 scripts/validate_submission.py "$(FILE)"

release-check: validate-rubric validate-example test
