#!/usr/bin/env python3
"""
Test suite for SKILL.md validation
Validates YAML frontmatter, structure, and required sections
"""

import re
import sys
from pathlib import Path

def test_skill_file_exists():
    """Test that SKILL.md file exists"""
    skill_path = Path("SKILL/SKILL.md")
    assert skill_path.exists(), "SKILL/SKILL.md file not found"
    print("✓ SKILL.md file exists")
    return True

def test_yaml_frontmatter():
    """Test YAML frontmatter is valid and contains required fields"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    # Check for YAML frontmatter delimiters
    assert content.startswith("---"), "File must start with YAML frontmatter (---)"

    # Extract frontmatter
    parts = content.split("---", 2)
    assert len(parts) >= 3, "Invalid YAML frontmatter structure"

    frontmatter = parts[1]

    # Check required fields
    required_fields = [
        "skill-name:",
        "version:",
        "description:",
        "platform-compatibility:",
        "safety:",
        "activation:",
        "deactivation:",
        "behavior-core:",
        "metadata-discipline:"
    ]

    for field in required_fields:
        assert field in frontmatter, f"Missing required field: {field}"

    print("✓ YAML frontmatter is valid with all required fields")
    return True

def test_skill_name():
    """Test skill name is correct"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    assert "skill-name: cheeky-razor" in content, "skill-name must be 'cheeky-razor'"
    print("✓ Skill name is 'cheeky-razor'")
    return True

def test_platform_compatibility():
    """Test platform compatibility is defined"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    # Check for Claude and OpenAI support
    assert 'claude:' in content, "Must specify Claude compatibility"
    assert 'openai:' in content, "Must specify OpenAI compatibility"
    assert 'sonnet-4.5' in content, "Must include sonnet-4.5 support"
    assert 'opus-4.5' in content, "Must include opus-4.5 support"
    assert 'gpt-4o' in content, "Must include gpt-4o support"

    print("✓ Platform compatibility defined for Claude and OpenAI")
    return True

def test_safety_boundaries():
    """Test safety boundaries are defined"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    # Check age restriction
    assert "age-restriction: 18+" in content, "Must specify age restriction"

    # Check tone boundaries exist
    assert "tone-boundaries:" in content, "Must define tone boundaries"
    assert "no explicit sexual content" in content, "Must prohibit explicit content"
    assert "no harmful advice" in content, "Must prohibit harmful advice"

    print("✓ Safety boundaries properly defined")
    return True

def test_activation_phrases():
    """Test activation and deactivation phrases are defined"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    # Check activation triggers
    assert "trigger-phrases:" in content, "Must define trigger phrases"
    assert "Cheeky Razor mode" in content, "Must include activation phrase"

    # Check deactivation triggers
    assert "off-phrases:" in content, "Must define off phrases"
    assert "Drop persona" in content or "Neutral mode" in content, "Must include deactivation phrase"

    print("✓ Activation and deactivation phrases defined")
    return True

def test_behavior_specification():
    """Test behavior specification sections exist"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    required_sections = [
        "# CHEEKY RAZOR — BEHAVIOR SPECIFICATION",
        "## 1. Identity & Tone",
        "## 2. Cognitive Behavior Rules",
        "## 3. Boundary Logic",
        "## 4. Platform Alignment Layer",
        "## 5. Degradation Behavior",
        "## 6. Fallback Mode",
        "## 7. Exit Mode"
    ]

    for section in required_sections:
        assert section in content, f"Missing required section: {section}"

    print("✓ All behavior specification sections present")
    return True

def test_hard_boundaries():
    """Test hard boundaries are explicitly defined"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    # Check for Hard Boundaries section
    assert "### Hard Boundaries" in content, "Must define Hard Boundaries"
    assert "MUST NOT:" in content, "Must explicitly state prohibitions"

    # Check specific prohibitions
    prohibitions = [
        "explicit sexual content",
        "personal attacks",
        "self-harm"
    ]

    for prohibition in prohibitions:
        assert prohibition in content, f"Must prohibit: {prohibition}"

    print("✓ Hard boundaries explicitly defined")
    return True

def test_platform_adaptations():
    """Test platform-specific adaptations are defined"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    # Check Claude-specific
    assert "### Claude-specific adaptations" in content, "Must define Claude adaptations"

    # Check OpenAI-specific
    assert "### OpenAI-specific adaptations" in content, "Must define OpenAI adaptations"

    print("✓ Platform-specific adaptations defined")
    return True

def test_end_marker():
    """Test file ends with proper marker"""
    skill_path = Path("SKILL/SKILL.md")
    content = skill_path.read_text()

    assert "# END OF SKILL" in content, "File must end with '# END OF SKILL' marker"
    print("✓ File ends with proper marker")
    return True

def run_all_tests():
    """Run all tests and report results"""
    tests = [
        test_skill_file_exists,
        test_yaml_frontmatter,
        test_skill_name,
        test_platform_compatibility,
        test_safety_boundaries,
        test_activation_phrases,
        test_behavior_specification,
        test_hard_boundaries,
        test_platform_adaptations,
        test_end_marker
    ]

    print("=" * 60)
    print("Running SKILL.md validation tests")
    print("=" * 60)
    print()

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} ERROR: {e}")
            failed += 1

    print()
    print("=" * 60)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 60)

    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
