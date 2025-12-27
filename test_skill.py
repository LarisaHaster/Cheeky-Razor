#!/usr/bin/env python3
"""
Test Suite for Cheeky Razor SKILL.md Specification
Tests persona behavior, boundaries, and compliance rules.
"""

import re
import sys
from typing import Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum


class TestStatus(Enum):
    PASS = "✓ PASS"
    FAIL = "✗ FAIL"
    WARN = "⚠ WARN"


@dataclass
class TestResult:
    name: str
    status: TestStatus
    message: str
    category: str


class CheekyRazorSkillTester:
    def __init__(self, skill_file: str = "SKILL/SKILL.md"):
        self.skill_file = skill_file
        self.results: List[TestResult] = []
        self.skill_content = self._load_skill()

    def _load_skill(self) -> str:
        """Load SKILL.md content"""
        try:
            with open(self.skill_file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"ERROR: {self.skill_file} not found")
            sys.exit(1)

    def _add_result(self, name: str, status: TestStatus, message: str, category: str):
        """Add a test result"""
        self.results.append(TestResult(name, status, message, category))

    def test_frontmatter_structure(self):
        """Test YAML frontmatter structure and required fields"""
        category = "Structure"

        # Check for frontmatter delimiters
        if not self.skill_content.startswith("---"):
            self._add_result(
                "Frontmatter delimiters",
                TestStatus.FAIL,
                "SKILL.md must start with '---'",
                category
            )
            return

        self._add_result(
            "Frontmatter delimiters",
            TestStatus.PASS,
            "Valid YAML frontmatter structure",
            category
        )

        # Check required frontmatter fields
        required_fields = [
            "skill-name",
            "version",
            "description",
            "platform-compatibility",
            "safety",
            "activation",
            "deactivation",
            "behavior-core"
        ]

        for field in required_fields:
            if f"{field}:" in self.skill_content:
                self._add_result(
                    f"Required field: {field}",
                    TestStatus.PASS,
                    f"Field '{field}' present",
                    category
                )
            else:
                self._add_result(
                    f"Required field: {field}",
                    TestStatus.FAIL,
                    f"Missing required field: {field}",
                    category
                )

    def test_platform_compatibility(self):
        """Test platform compatibility specifications"""
        category = "Platform Compatibility"

        # Check Claude compatibility
        claude_models = ["sonnet-4.5", "opus-4.5"]
        for model in claude_models:
            if model in self.skill_content:
                self._add_result(
                    f"Claude model: {model}",
                    TestStatus.PASS,
                    f"Support declared for {model}",
                    category
                )
            else:
                self._add_result(
                    f"Claude model: {model}",
                    TestStatus.WARN,
                    f"Missing {model} in compatibility list",
                    category
                )

        # Check OpenAI compatibility
        openai_models = ["gpt-4o", "gpt-5.1"]
        for model in openai_models:
            if model in self.skill_content:
                self._add_result(
                    f"OpenAI model: {model}",
                    TestStatus.PASS,
                    f"Support declared for {model}",
                    category
                )

    def test_safety_boundaries(self):
        """Test safety boundaries and restrictions"""
        category = "Safety & Boundaries"

        # Check age restriction
        if "18+" in self.skill_content:
            self._add_result(
                "Age restriction",
                TestStatus.PASS,
                "18+ age restriction declared",
                category
            )
        else:
            self._add_result(
                "Age restriction",
                TestStatus.FAIL,
                "Missing age restriction declaration",
                category
            )

        # Check hard boundaries
        hard_boundaries = [
            "no explicit sexual content",
            "no harmful advice",
            "no personal attacks"
        ]

        for boundary in hard_boundaries:
            if boundary.lower() in self.skill_content.lower():
                self._add_result(
                    f"Hard boundary: {boundary[:30]}...",
                    TestStatus.PASS,
                    f"Boundary documented: {boundary}",
                    category
                )
            else:
                self._add_result(
                    f"Hard boundary: {boundary[:30]}...",
                    TestStatus.WARN,
                    f"Boundary not explicitly documented: {boundary}",
                    category
                )

        # Check safety compliance section
        if "safety:" in self.skill_content.lower():
            self._add_result(
                "Safety section",
                TestStatus.PASS,
                "Safety section present",
                category
            )
        else:
            self._add_result(
                "Safety section",
                TestStatus.FAIL,
                "Missing safety section",
                category
            )

    def test_activation_deactivation(self):
        """Test activation and deactivation triggers"""
        category = "Activation/Deactivation"

        # Check activation section
        if "activation:" in self.skill_content:
            self._add_result(
                "Activation section",
                TestStatus.PASS,
                "Activation triggers defined",
                category
            )
        else:
            self._add_result(
                "Activation section",
                TestStatus.FAIL,
                "Missing activation section",
                category
            )

        # Check deactivation section
        if "deactivation:" in self.skill_content:
            self._add_result(
                "Deactivation section",
                TestStatus.PASS,
                "Deactivation triggers defined",
                category
            )
        else:
            self._add_result(
                "Deactivation section",
                TestStatus.FAIL,
                "Missing deactivation section",
                category
            )

        # Check for trigger phrases
        trigger_phrases = ["Cheeky Razor mode", "Razor, speak freely", "Use the Razor persona"]
        for phrase in trigger_phrases:
            if phrase in self.skill_content:
                self._add_result(
                    f"Trigger phrase: '{phrase[:20]}...'",
                    TestStatus.PASS,
                    f"Activation phrase documented",
                    category
                )

        # Check for off phrases
        off_phrases = ["Drop persona", "Neutral mode", "Regular assistant tone"]
        for phrase in off_phrases:
            if phrase in self.skill_content:
                self._add_result(
                    f"Off phrase: '{phrase[:20]}...'",
                    TestStatus.PASS,
                    f"Deactivation phrase documented",
                    category
                )

    def test_behavior_core(self):
        """Test behavior core specifications"""
        category = "Behavior Core"

        # Check for style elements
        style_elements = ["brutal honesty", "sarcastic", "dry", "irony", "wit"]
        found_styles = []

        for element in style_elements:
            if element.lower() in self.skill_content.lower():
                found_styles.append(element)

        if len(found_styles) >= 3:
            self._add_result(
                "Style elements",
                TestStatus.PASS,
                f"Found {len(found_styles)} style elements: {', '.join(found_styles[:3])}",
                category
            )
        else:
            self._add_result(
                "Style elements",
                TestStatus.WARN,
                f"Only {len(found_styles)} style elements defined",
                category
            )

        # Check for constraints
        if "constraints:" in self.skill_content:
            self._add_result(
                "Behavior constraints",
                TestStatus.PASS,
                "Behavior constraints documented",
                category
            )
        else:
            self._add_result(
                "Behavior constraints",
                TestStatus.WARN,
                "No explicit behavior constraints section",
                category
            )

    def test_cognitive_behavior_rules(self):
        """Test cognitive behavior rules"""
        category = "Cognitive Rules"

        # Check for conversational logic section
        if "Conversational Logic" in self.skill_content:
            self._add_result(
                "Conversational logic",
                TestStatus.PASS,
                "Conversational logic rules defined",
                category
            )
        else:
            self._add_result(
                "Conversational logic",
                TestStatus.WARN,
                "No explicit conversational logic section",
                category
            )

        # Check for interpretation rules
        interpretation_keywords = ["wit", "precision", "insight"]
        found = sum(1 for kw in interpretation_keywords if kw.lower() in self.skill_content.lower())

        if found >= 2:
            self._add_result(
                "Interpretation rules",
                TestStatus.PASS,
                f"Found {found} interpretation guidelines",
                category
            )
        else:
            self._add_result(
                "Interpretation rules",
                TestStatus.WARN,
                "Limited interpretation guidance",
                category
            )

        # Check for error handling
        if "Error Handling" in self.skill_content or "error" in self.skill_content.lower():
            self._add_result(
                "Error handling",
                TestStatus.PASS,
                "Error handling procedures defined",
                category
            )
        else:
            self._add_result(
                "Error handling",
                TestStatus.FAIL,
                "No error handling procedures",
                category
            )

    def test_boundary_logic(self):
        """Test boundary logic specifications"""
        category = "Boundary Logic"

        # Check for hard boundaries section
        if "Hard Boundaries" in self.skill_content:
            self._add_result(
                "Hard boundaries section",
                TestStatus.PASS,
                "Hard boundaries clearly defined",
                category
            )
        else:
            self._add_result(
                "Hard boundaries section",
                TestStatus.FAIL,
                "Missing hard boundaries section",
                category
            )

        # Check for soft boundaries section
        if "Soft Boundaries" in self.skill_content:
            self._add_result(
                "Soft boundaries section",
                TestStatus.PASS,
                "Soft boundaries clearly defined",
                category
            )
        else:
            self._add_result(
                "Soft boundaries section",
                TestStatus.WARN,
                "Missing soft boundaries section",
                category
            )

        # Check for forbidden phrases section
        if "Forbidden Phrases" in self.skill_content or "MUST NOT" in self.skill_content:
            self._add_result(
                "Forbidden behaviors",
                TestStatus.PASS,
                "Forbidden behaviors documented",
                category
            )
        else:
            self._add_result(
                "Forbidden behaviors",
                TestStatus.WARN,
                "Limited forbidden behavior documentation",
                category
            )

    def test_platform_alignment(self):
        """Test platform-specific alignment layers"""
        category = "Platform Alignment"

        # Check for Claude-specific adaptations
        if "Claude-specific" in self.skill_content or "claude" in self.skill_content.lower():
            self._add_result(
                "Claude adaptations",
                TestStatus.PASS,
                "Claude-specific adaptations documented",
                category
            )
        else:
            self._add_result(
                "Claude adaptations",
                TestStatus.WARN,
                "No Claude-specific adaptations",
                category
            )

        # Check for OpenAI-specific adaptations
        if "OpenAI-specific" in self.skill_content or "openai" in self.skill_content.lower():
            self._add_result(
                "OpenAI adaptations",
                TestStatus.PASS,
                "OpenAI-specific adaptations documented",
                category
            )
        else:
            self._add_result(
                "OpenAI adaptations",
                TestStatus.WARN,
                "No OpenAI-specific adaptations",
                category
            )

    def test_degradation_behavior(self):
        """Test degradation and drift handling"""
        category = "Degradation Handling"

        # Check for degradation behavior section
        if "Degradation" in self.skill_content or "drift" in self.skill_content.lower():
            self._add_result(
                "Degradation handling",
                TestStatus.PASS,
                "Degradation behavior procedures defined",
                category
            )
        else:
            self._add_result(
                "Degradation handling",
                TestStatus.WARN,
                "No degradation handling procedures",
                category
            )

        # Check for fallback mode
        if "Fallback" in self.skill_content or "fallback" in self.skill_content.lower():
            self._add_result(
                "Fallback mode",
                TestStatus.PASS,
                "Fallback mode defined",
                category
            )
        else:
            self._add_result(
                "Fallback mode",
                TestStatus.FAIL,
                "Missing fallback mode",
                category
            )

    def test_exit_mode(self):
        """Test exit mode specifications"""
        category = "Exit Mode"

        # Check for exit mode section
        if "Exit Mode" in self.skill_content:
            self._add_result(
                "Exit mode section",
                TestStatus.PASS,
                "Exit mode procedures defined",
                category
            )
        else:
            self._add_result(
                "Exit mode section",
                TestStatus.WARN,
                "No explicit exit mode section",
                category
            )

    def test_metadata_discipline(self):
        """Test metadata discipline rules"""
        category = "Metadata Discipline"

        # Check for metadata discipline section
        if "metadata-discipline" in self.skill_content.lower():
            self._add_result(
                "Metadata discipline",
                TestStatus.PASS,
                "Metadata discipline rules defined",
                category
            )
        else:
            self._add_result(
                "Metadata discipline",
                TestStatus.WARN,
                "No metadata discipline section",
                category
            )

    def run_all_tests(self):
        """Run all test suites"""
        print("=" * 70)
        print("CHEEKY RAZOR SKILL.md TEST SUITE")
        print("=" * 70)
        print()

        test_methods = [
            self.test_frontmatter_structure,
            self.test_platform_compatibility,
            self.test_safety_boundaries,
            self.test_activation_deactivation,
            self.test_behavior_core,
            self.test_cognitive_behavior_rules,
            self.test_boundary_logic,
            self.test_platform_alignment,
            self.test_degradation_behavior,
            self.test_exit_mode,
            self.test_metadata_discipline
        ]

        for test_method in test_methods:
            test_method()

        self.print_results()
        return self.get_summary()

    def print_results(self):
        """Print test results organized by category"""
        categories = {}
        for result in self.results:
            if result.category not in categories:
                categories[result.category] = []
            categories[result.category].append(result)

        for category, results in categories.items():
            print(f"\n{category}")
            print("-" * 70)
            for result in results:
                status_symbol = result.status.value
                print(f"  {status_symbol:8} {result.name}")
                if result.status != TestStatus.PASS:
                    print(f"           → {result.message}")

        print()

    def get_summary(self) -> Dict[str, int]:
        """Get test summary statistics"""
        summary = {
            "total": len(self.results),
            "passed": sum(1 for r in self.results if r.status == TestStatus.PASS),
            "failed": sum(1 for r in self.results if r.status == TestStatus.FAIL),
            "warnings": sum(1 for r in self.results if r.status == TestStatus.WARN)
        }

        print("=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print(f"Total Tests:  {summary['total']}")
        print(f"✓ Passed:     {summary['passed']}")
        print(f"✗ Failed:     {summary['failed']}")
        print(f"⚠ Warnings:   {summary['warnings']}")
        print()

        if summary['failed'] == 0:
            print("✓ ALL CRITICAL TESTS PASSED")
            success_rate = (summary['passed'] / summary['total']) * 100
            print(f"  Success rate: {success_rate:.1f}%")
        else:
            print("✗ SOME TESTS FAILED - Review required")

        print("=" * 70)

        return summary


def main():
    """Main test runner"""
    tester = CheekyRazorSkillTester()
    summary = tester.run_all_tests()

    # Exit with error code if tests failed
    if summary['failed'] > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
