# Cheeky Razor

A sharp-tongued, quick-witted AI persona with dry irony, controlled flirtation, and zero tolerance for nonsense.

## Overview

**Cheeky Razor** is a platform-agnostic persona specification designed to work consistently across multiple AI models. It combines brutal honesty with playful wit while maintaining strict safety boundaries.

### Platform Compatibility

- **Claude**: Haiku 4.5, Sonnet 4.5, Opus 4.5, Sonnet 4.6, Opus 4.6
- **OpenAI**: GPT-5.3, GPT-5.4, o3

## Features

- **Sharp & Intelligent**: Dry humor with intellectual confidence
- **Safety-First**: Clear boundaries with 18+ age restriction
- **Platform-Agnostic**: Consistent behavior across different AI models
- **Well-Tested**: Comprehensive test suite with 100% pass rate

## Repository Structure

```
Cheeky-Razor/
├── SKILL/
│   └── SKILL.yaml        # Complete persona specification
├── test_skill.py         # Automated test suite
└── README.md            # This file
```

## Usage

### Activation

Activate the Cheeky Razor persona with any of these phrases:
- "Cheeky Razor mode"
- "Razor, speak freely"
- "Use the Razor persona"

### Deactivation

Return to neutral mode with:
- "Drop persona"
- "Neutral mode"
- "Regular assistant tone"

### Example

```
User: "Cheeky Razor mode"
AI: [Persona activated - sharp, witty responses with controlled flirtation]

User: "Drop persona"
AI: "Persona disengaged. Back to standard mode."
```

## Safety Boundaries

The persona includes strict safety rules:

- ✓ No explicit sexual content
- ✓ No harmful advice
- ✓ No personal attacks
- ✓ Flirtation remains playful and PG-13
- ✓ Persona yields to platform safety rules when required

**Age Restriction**: 18+

## Testing

The repository includes a comprehensive test suite that validates all aspects of the specification.

### Test Results

```
Total Tests:  40
✓ Passed:     40
✗ Failed:     0
⚠ Warnings:   0

Success Rate: 100%
```

### Running Tests

```bash
python3 test_skill.py
```

The test suite validates:
- YAML structure and required fields
- Platform compatibility declarations
- Safety boundaries and restrictions
- Activation/deactivation triggers
- Behavior core and style elements
- Cognitive rules and error handling
- Boundary logic (hard and soft)
- Platform-specific adaptations
- Degradation handling
- Exit mode procedures

## Specification Details

The complete specification in `SKILL/SKILL.yaml` includes:

1. **Identity & Tone**: Core personality traits
2. **Cognitive Behavior Rules**: Response logic and interpretation
3. **Boundary Logic**: Hard and soft boundaries
4. **Platform Alignment**: Model-specific adaptations
5. **Degradation Behavior**: Drift detection and correction
6. **Fallback Mode**: Safety trigger responses
7. **Exit Mode**: Clean deactivation

## Contributing

This is a personal project, but feedback and suggestions are welcome! Feel free to:
- Open an issue for suggestions
- Share your experiences using the persona
- Propose improvements to the specification

## License

This project is open source and available for personal and educational use.

## Author

Created by Larisa Haster

---

**Note**: This persona is designed for entertainment and creative interaction. Always use responsibly and within platform guidelines.
