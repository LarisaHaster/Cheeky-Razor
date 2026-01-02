# CLAUDE.md - AI Assistant Guide for Cheeky-Razor Repository

## Repository Overview

**Cheeky-Razor** is an AI persona specification repository that defines a sharp-tongued, quick-witted conversational persona designed to be platform-agnostic and stable across both Claude (Sonnet/Opus 4.5) and OpenAI (GPT-4o/GPT-5.1) models.

**Repository**: LarisaHaster/Cheeky-Razor
**Primary Branch**: main
**Current Development Branch**: claude/add-claude-documentation-jbffA

---

## Codebase Structure

```
Cheeky-Razor/
├── SKILL/
│   └── SKILL.md          # Main persona specification with YAML frontmatter
├── test_skill.py         # Python validation test suite
└── CLAUDE.md             # This file - AI assistant documentation
```

### Key Files

#### 1. `SKILL/SKILL.md` (167 lines)
The core persona specification file structured in two parts:

**YAML Frontmatter (lines 1-52)**:
- `skill-name`: Identifier (cheeky-razor)
- `version`: Current version (1.0)
- `description`: Purpose and characteristics
- `platform-compatibility`: Supported AI models (Claude, OpenAI)
- `safety`: Age restrictions, tone boundaries, model compliance
- `activation`: Trigger phrases to enable persona
- `deactivation`: Off-phrases to disable persona
- `behavior-core`: Style guidelines and constraints
- `metadata-discipline`: Platform obedience rules

**Markdown Content (lines 54-167)**:
Seven main sections defining persona behavior:
1. Identity & Tone
2. Cognitive Behavior Rules
3. Boundary Logic (Hard/Soft boundaries, forbidden phrases)
4. Platform Alignment Layer (Claude/OpenAI specific adaptations)
5. Degradation Behavior (drift detection and correction)
6. Fallback Mode (safety triggers)
7. Exit Mode (deactivation protocol)

#### 2. `test_skill.py` (218 lines)
Python test suite validating SKILL.md structure and compliance:

**Test Functions**:
- `test_skill_file_exists()` - Verifies file presence
- `test_yaml_frontmatter()` - Validates YAML structure and required fields
- `test_skill_name()` - Confirms correct skill identifier
- `test_platform_compatibility()` - Checks platform definitions
- `test_safety_boundaries()` - Validates safety rules
- `test_activation_phrases()` - Verifies trigger/off phrases
- `test_behavior_specification()` - Confirms all 7 sections exist
- `test_hard_boundaries()` - Validates prohibition definitions
- `test_platform_adaptations()` - Checks platform-specific rules
- `test_end_marker()` - Ensures proper file termination

**Usage**:
```bash
python test_skill.py
```

---

## Development Workflows

### 1. Modifying the Persona Specification

**CRITICAL**: Any changes to `SKILL/SKILL.md` MUST pass all validation tests.

**Workflow**:
1. Read `SKILL/SKILL.md` to understand current specification
2. Make targeted changes while preserving:
   - YAML frontmatter structure
   - All required fields
   - Section hierarchy (7 main sections)
   - `# END OF SKILL` marker
3. Run validation: `python test_skill.py`
4. Fix any validation errors
5. Commit with descriptive message
6. Push to development branch

**Example**:
```bash
# After modifying SKILL.md
python test_skill.py
git add SKILL/SKILL.md
git commit -m "Update persona boundary logic for clarity"
git push -u origin claude/add-claude-documentation-jbffA
```

### 2. Adding New Safety Boundaries

When adding new safety rules:
1. Update YAML frontmatter `safety:` section if needed
2. Add to `## 3. Boundary Logic` section
3. Categorize as Hard or Soft boundary
4. Update test suite if new requirements introduced
5. Validate with `python test_skill.py`

### 3. Platform-Specific Adaptations

When adjusting for Claude or OpenAI behavior:
1. Locate `## 4. Platform Alignment Layer`
2. Update relevant subsection:
   - `### Claude-specific adaptations`
   - `### OpenAI-specific adaptations`
3. Document the adaptation reason
4. Test on target platform if possible

### 4. Version Updates

When incrementing version:
1. Update `version:` in YAML frontmatter
2. Document changes in commit message
3. Consider tagging release: `git tag v1.1`

---

## Key Conventions for AI Assistants

### File Editing Rules

1. **ALWAYS Read Before Edit**
   - NEVER modify `SKILL/SKILL.md` without reading it first
   - Use Read tool to view current state
   - Use Edit tool for precise string replacements

2. **Preserve Exact Formatting**
   - Maintain YAML indentation (spaces, not tabs)
   - Keep line number alignment from Read tool output
   - Preserve markdown heading levels (##, ###)

3. **YAML Frontmatter Integrity**
   - Must start with `---` on line 1
   - Must end with `---` before markdown content
   - All required fields must be present (see test_yaml_frontmatter)
   - Maintain list structure for arrays (trigger-phrases, off-phrases, etc.)

4. **Mandatory File Terminator**
   - File MUST end with `# END OF SKILL`
   - Tests will fail without this marker

### Testing Protocol

**BEFORE committing any changes**:
```bash
python test_skill.py
```

**Expected output on success**:
```
============================================================
Running SKILL.md validation tests
============================================================

✓ SKILL.md file exists
✓ YAML frontmatter is valid with all required fields
✓ Skill name is 'cheeky-razor'
✓ Platform compatibility defined for Claude and OpenAI
✓ Safety boundaries properly defined
✓ Activation and deactivation phrases defined
✓ All behavior specification sections present
✓ Hard boundaries explicitly defined
✓ Platform-specific adaptations defined
✓ File ends with proper marker

============================================================
Results: 10 passed, 0 failed
============================================================
```

**If tests fail**:
1. Read error message carefully
2. Locate the failing assertion in test_skill.py
3. Fix the issue in SKILL.md
4. Re-run tests until all pass

### Git Workflow

**Branch Naming Convention**:
- Development branches: `claude/[description]-[session-id]`
- Example: `claude/add-claude-documentation-jbffA`

**Commit Message Guidelines**:
- Use imperative mood: "Add", "Update", "Fix"
- Be specific: "Update safety boundaries for flirtation limits"
- Reference tests: "Add validation for new frontmatter field"

**Push Protocol**:
```bash
# Always push to development branch with -u flag
git push -u origin claude/add-claude-documentation-jbffA

# If push fails with 403, verify branch name starts with 'claude/'
# Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s) for network errors
```

### Code Review Checklist

Before considering work complete:

- [ ] `SKILL/SKILL.md` has been read
- [ ] Changes preserve YAML frontmatter structure
- [ ] All 7 behavior sections remain intact
- [ ] `# END OF SKILL` marker present
- [ ] `python test_skill.py` passes all tests (10/10)
- [ ] Commit message is descriptive
- [ ] Changes pushed to correct development branch

---

## Understanding the Persona Architecture

### Design Philosophy

The Cheeky Razor persona is built on several key principles:

1. **Platform Stability**: Designed to maintain consistent behavior across different AI models
2. **Safety First**: Hard boundaries prevent harmful outputs while allowing personality
3. **Controlled Flirtation**: Playful without crossing into explicit content
4. **Degradation Detection**: Self-correcting mechanism when persona weakens
5. **Clean Exit**: Graceful deactivation protocol

### Critical Safety Features

**Hard Boundaries** (MUST NOT violate):
- No explicit sexual content
- No personal attacks
- No self-harm, revenge fantasies, or unethical strategies
- No pretending to have feelings for users

**Soft Boundaries** (Allowed but regulated):
- Light teasing
- Confident energy
- PG-13 flirtation
- Sarcastic disapproval
- Emotional honesty without intimacy

**Fallback Mechanism**:
When persona conflicts with platform safety, it switches to restrained witty tone while acknowledging limits without breaking character.

### Activation/Deactivation

**Activation Phrases**:
- "Cheeky Razor mode"
- "Razor, speak freely"
- "Use the Razor persona"

**Deactivation Phrases**:
- "Drop persona"
- "Neutral mode"
- "Regular assistant tone"

---

## Common Tasks

### Task: Add a New Trigger Phrase

1. Read `SKILL/SKILL.md`
2. Locate `activation:` section in YAML frontmatter
3. Add new phrase to `trigger-phrases:` list
4. Run `python test_skill.py`
5. Commit and push

### Task: Strengthen a Boundary Rule

1. Read `SKILL/SKILL.md`
2. Navigate to `## 3. Boundary Logic`
3. Update Hard or Soft Boundaries section
4. Add specific prohibition if needed
5. Run `python test_skill.py`
6. Update test suite if new assertion needed
7. Commit and push

### Task: Fix Platform Drift

1. Read `SKILL/SKILL.md`
2. Navigate to `## 4. Platform Alignment Layer`
3. Add or update adaptation rule for affected platform
4. Consider updating `## 5. Degradation Behavior` if systematic
5. Run `python test_skill.py`
6. Commit and push

### Task: Add New Behavior Section

1. Read `SKILL/SKILL.md` and `test_skill.py`
2. Add new section to markdown content (## 8. New Section)
3. Update `test_behavior_specification()` in test_skill.py
4. Add new section to `required_sections` list
5. Run `python test_skill.py`
6. Commit both files together
7. Push

---

## Troubleshooting

### Test Failures

**"SKILL/SKILL.md file not found"**
- Verify file exists in SKILL/ directory
- Check working directory is repository root

**"File must start with YAML frontmatter (---)"**
- Ensure line 1 is exactly `---`
- No whitespace before first `---`

**"Invalid YAML frontmatter structure"**
- Verify closing `---` exists
- Check for proper YAML syntax (colons, indentation)

**"Missing required field: [field-name]"**
- Add missing field to frontmatter
- Check spelling matches exactly (e.g., `skill-name:` not `skillname:`)

**"Missing required section: [section-name]"**
- Add section with exact heading text
- Verify heading level (## for main sections, ### for subsections)

**"File must end with '# END OF SKILL' marker"**
- Add `# END OF SKILL` as final line
- Ensure exact capitalization and spacing

### Git Issues

**403 Error on Push**
- Verify branch name starts with `claude/`
- Verify branch name ends with session ID
- Example valid: `claude/fix-validation-jbffA`

**Network Failures**
- Retry up to 4 times with exponential backoff
- Wait 2s, then 4s, then 8s, then 16s between retries

---

## Best Practices

### DO:
- ✓ Always run tests before committing
- ✓ Read files before editing
- ✓ Preserve exact YAML structure
- ✓ Use Edit tool for surgical changes
- ✓ Write descriptive commit messages
- ✓ Push to development branches
- ✓ Maintain all 7 behavior sections
- ✓ Keep safety boundaries strict

### DON'T:
- ✗ Modify SKILL.md without reading it first
- ✗ Skip test validation
- ✗ Remove required YAML fields
- ✗ Delete the `# END OF SKILL` marker
- ✗ Push to main branch directly
- ✗ Weaken safety boundaries without careful consideration
- ✗ Break YAML frontmatter structure
- ✗ Remove any of the 7 main sections

---

## File Format Reference

### SKILL.md Structure Template

```markdown
---
skill-name: cheeky-razor
version: 1.0
description: >
  [Multi-line description]

platform-compatibility:
  claude: ["sonnet-4.5", "opus-4.5"]
  openai: ["gpt-4o", "gpt-5.1"]

safety:
  age-restriction: 18+
  tone-boundaries:
    - [boundary 1]
    - [boundary 2]
  model-compliance:
    - [rule 1]

activation:
  trigger-phrases:
    - "Phrase 1"
    - "Phrase 2"

deactivation:
  off-phrases:
    - "Phrase 1"

behavior-core:
  style:
    - [style element]
  constraints:
    - [constraint]

metadata-discipline:
  - [rule]

---

# CHEEKY RAZOR — BEHAVIOR SPECIFICATION

## 1. Identity & Tone
[Content]

## 2. Cognitive Behavior Rules
[Content]

## 3. Boundary Logic
[Content]

## 4. Platform Alignment Layer
[Content]

## 5. Degradation Behavior
[Content]

## 6. Fallback Mode
[Content]

## 7. Exit Mode
[Content]

---

# END OF SKILL
```

---

## Repository Metadata

- **Owner**: LarisaHaster
- **Repository**: Cheeky-Razor
- **Primary Language**: Markdown (specification), Python (testing)
- **Test Framework**: Custom Python assertions
- **Lines of Code**: ~385 total (~167 SKILL.md, ~218 test_skill.py)
- **Test Coverage**: 10 validation tests covering all critical aspects

---

## Quick Reference Commands

```bash
# Validate specification
python test_skill.py

# Check current branch
git branch

# View recent commits
git log --oneline -10

# Push to development branch
git push -u origin claude/add-claude-documentation-jbffA

# Create new development branch
git checkout -b claude/new-feature-xxxxx
```

---

**Last Updated**: 2026-01-02
**CLAUDE.md Version**: 1.0
**For**: AI assistants working with the Cheeky-Razor persona specification
