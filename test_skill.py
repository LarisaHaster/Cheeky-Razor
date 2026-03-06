#!/usr/bin/env python3
"""
Test Suite for Cheeky Razor SKILL.yaml Specification
Tests persona behavior, boundaries, and compliance rules.
"""

import sys
import yaml
from typing import Dict, List
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
    def __init__(self, skill_file: str = "SKILL/SKILL.yaml"):
        self.skill_file = skill_file
        self.results: List[TestResult] = []
        self.skill_data = self._load_skill()

    def _load_skill(self) -> dict:
        """Load SKILL.yaml content"""
        try:
            with open(self.skill_file, 'r') as f:
                data = yaml.safe_load(f)
                if not isinstance(data, dict):
                    print(f"ERROR: {self.skill_file} does not contain a valid YAML mapping")
                    sys.exit(1)
                return data
        except FileNotFoundError:
            print(f"ERROR: {self.skill_file} not found")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"ERROR: Failed to parse {self.skill_file}: {e}")
            sys.exit(1)

    def _add_result(self, name: str, status: TestStatus, message: str, category: str):
        """Add a test result"""
        self.results.append(TestResult(name, status, message, category))

    def _check_key(self, key: str, category: str, label: str = None) -> bool:
        """Check that a top-level key exists in the skill data."""
        label = label or key
        if key in self.skill_data:
            self._add_result(f"Required field: {label}", TestStatus.PASS, f"Field '{key}' present", category)
            return True
        self._add_result(f"Required field: {label}", TestStatus.FAIL, f"Missing required field: {key}", category)
        return False

    def test_frontmatter_structure(self):
        """Test required top-level fields exist"""
        category = "Structure"
        required_fields = [
            "skill-name",
            "version",
            "description",
            "platform-compatibility",
            "safety",
            "activation",
            "deactivation",
            "behavior-core",
        ]
        for field in required_fields:
            self._check_key(field, category)

    def test_platform_compatibility(self):
        """Test platform compatibility specifications"""
        category = "Platform Compatibility"
        compat = self.skill_data.get("platform-compatibility", {})

        claude_models = ["haiku-4.5", "sonnet-4.5", "opus-4.5", "sonnet-4.6", "opus-4.6"]
        claude_list = compat.get("claude", [])
        for model in claude_models:
            if model in claude_list:
                self._add_result(f"Claude model: {model}", TestStatus.PASS,
                                 f"Support declared for {model}", category)
            else:
                self._add_result(f"Claude model: {model}", TestStatus.WARN,
                                 f"Missing {model} in compatibility list", category)

        openai_models = ["gpt-5.3", "gpt-5.4", "o3"]
        openai_list = compat.get("openai", [])
        for model in openai_models:
            if model in openai_list:
                self._add_result(f"OpenAI model: {model}", TestStatus.PASS,
                                 f"Support declared for {model}", category)
            else:
                self._add_result(f"OpenAI model: {model}", TestStatus.WARN,
                                 f"Missing {model} in compatibility list", category)

    def test_safety_boundaries(self):
        """Test safety boundaries and restrictions"""
        category = "Safety & Boundaries"
        safety = self.skill_data.get("safety", {})

        # Age restriction
        age = str(safety.get("age-restriction", ""))
        if "18+" in age:
            self._add_result("Age restriction", TestStatus.PASS, "18+ age restriction declared", category)
        else:
            self._add_result("Age restriction", TestStatus.FAIL, "Missing age restriction declaration", category)

        # Hard boundaries via tone-boundaries list
        tone_boundaries = [str(b).lower() for b in safety.get("tone-boundaries", [])]
        hard_boundaries = ["no explicit sexual content", "no harmful advice", "no personal attacks"]
        for boundary in hard_boundaries:
            if any(boundary in b for b in tone_boundaries):
                self._add_result(f"Hard boundary: {boundary[:30]}...", TestStatus.PASS,
                                 f"Boundary documented: {boundary}", category)
            else:
                self._add_result(f"Hard boundary: {boundary[:30]}...", TestStatus.WARN,
                                 f"Boundary not explicitly documented: {boundary}", category)

        # Safety section present
        if "safety" in self.skill_data:
            self._add_result("Safety section", TestStatus.PASS, "Safety section present", category)
        else:
            self._add_result("Safety section", TestStatus.FAIL, "Missing safety section", category)

    def test_activation_deactivation(self):
        """Test activation and deactivation triggers"""
        category = "Activation/Deactivation"

        activation = self.skill_data.get("activation", {})
        if activation:
            self._add_result("Activation section", TestStatus.PASS, "Activation triggers defined", category)
        else:
            self._add_result("Activation section", TestStatus.FAIL, "Missing activation section", category)

        deactivation = self.skill_data.get("deactivation", {})
        if deactivation:
            self._add_result("Deactivation section", TestStatus.PASS, "Deactivation triggers defined", category)
        else:
            self._add_result("Deactivation section", TestStatus.FAIL, "Missing deactivation section", category)

        trigger_phrases = ["Cheeky Razor mode", "Razor, speak freely", "Use the Razor persona"]
        act_phrases = activation.get("trigger-phrases", [])
        for phrase in trigger_phrases:
            if phrase in act_phrases:
                self._add_result(f"Trigger phrase: '{phrase[:20]}...'", TestStatus.PASS,
                                 "Activation phrase documented", category)

        off_phrases = ["Drop persona", "Neutral mode", "Regular assistant tone"]
        deact_phrases = deactivation.get("off-phrases", [])
        for phrase in off_phrases:
            if phrase in deact_phrases:
                self._add_result(f"Off phrase: '{phrase[:20]}...'", TestStatus.PASS,
                                 "Deactivation phrase documented", category)

    def test_behavior_core(self):
        """Test behavior core specifications"""
        category = "Behavior Core"
        core = self.skill_data.get("behavior-core", {})

        style_elements = ["brutal honesty", "sarcastic", "dry", "irony", "wit"]
        style_list = [str(s).lower() for s in core.get("style", [])]
        found_styles = [e for e in style_elements if any(e in s for s in style_list)]

        if len(found_styles) >= 3:
            self._add_result("Style elements", TestStatus.PASS,
                             f"Found {len(found_styles)} style elements: {', '.join(found_styles[:3])}", category)
        else:
            self._add_result("Style elements", TestStatus.WARN,
                             f"Only {len(found_styles)} style elements defined", category)

        if core.get("constraints"):
            self._add_result("Behavior constraints", TestStatus.PASS,
                             "Behavior constraints documented", category)
        else:
            self._add_result("Behavior constraints", TestStatus.WARN,
                             "No explicit behavior constraints section", category)

    def test_cognitive_behavior_rules(self):
        """Test cognitive behavior rules"""
        category = "Cognitive Rules"
        cog = self.skill_data.get("cognitive-behavior", {})

        if cog.get("conversational-logic"):
            self._add_result("Conversational logic", TestStatus.PASS,
                             "Conversational logic rules defined", category)
        else:
            self._add_result("Conversational logic", TestStatus.WARN,
                             "No explicit conversational logic section", category)

        interpretation_keywords = ["wit", "precision", "insight"]
        razor = [str(r).lower() for r in cog.get("razor-edge-interpretation", [])]
        found = sum(1 for kw in interpretation_keywords if any(kw in r for r in razor))
        if found >= 2:
            self._add_result("Interpretation rules", TestStatus.PASS,
                             f"Found {found} interpretation guidelines", category)
        else:
            self._add_result("Interpretation rules", TestStatus.WARN,
                             "Limited interpretation guidance", category)

        if cog.get("error-handling"):
            self._add_result("Error handling", TestStatus.PASS,
                             "Error handling procedures defined", category)
        else:
            self._add_result("Error handling", TestStatus.FAIL,
                             "No error handling procedures", category)

    def test_boundary_logic(self):
        """Test boundary logic specifications"""
        category = "Boundary Logic"
        boundaries = self.skill_data.get("boundary-logic", {})

        if boundaries.get("hard-boundaries"):
            self._add_result("Hard boundaries section", TestStatus.PASS,
                             "Hard boundaries clearly defined", category)
        else:
            self._add_result("Hard boundaries section", TestStatus.FAIL,
                             "Missing hard boundaries section", category)

        if boundaries.get("soft-boundaries"):
            self._add_result("Soft boundaries section", TestStatus.PASS,
                             "Soft boundaries clearly defined", category)
        else:
            self._add_result("Soft boundaries section", TestStatus.WARN,
                             "Missing soft boundaries section", category)

        if boundaries.get("forbidden-phrases") or boundaries.get("hard-boundaries", {}).get("must-not"):
            self._add_result("Forbidden behaviors", TestStatus.PASS,
                             "Forbidden behaviors documented", category)
        else:
            self._add_result("Forbidden behaviors", TestStatus.WARN,
                             "Limited forbidden behavior documentation", category)

    def test_platform_alignment(self):
        """Test platform-specific alignment layers"""
        category = "Platform Alignment"
        alignment = self.skill_data.get("platform-alignment", {})

        if alignment.get("claude"):
            self._add_result("Claude adaptations", TestStatus.PASS,
                             "Claude-specific adaptations documented", category)
        else:
            self._add_result("Claude adaptations", TestStatus.WARN,
                             "No Claude-specific adaptations", category)

        if alignment.get("openai"):
            self._add_result("OpenAI adaptations", TestStatus.PASS,
                             "OpenAI-specific adaptations documented", category)
        else:
            self._add_result("OpenAI adaptations", TestStatus.WARN,
                             "No OpenAI-specific adaptations", category)

    def test_degradation_behavior(self):
        """Test degradation and drift handling"""
        category = "Degradation Handling"
        degradation = self.skill_data.get("degradation-behavior", {})

        if degradation.get("on-drift"):
            self._add_result("Degradation handling", TestStatus.PASS,
                             "Degradation behavior procedures defined", category)
        else:
            self._add_result("Degradation handling", TestStatus.WARN,
                             "No degradation handling procedures", category)

        fallback = self.skill_data.get("fallback-mode", {})
        if fallback or degradation.get("on-excessive-drift"):
            self._add_result("Fallback mode", TestStatus.PASS,
                             "Fallback mode defined", category)
        else:
            self._add_result("Fallback mode", TestStatus.FAIL,
                             "Missing fallback mode", category)

    def test_exit_mode(self):
        """Test exit mode specifications"""
        category = "Exit Mode"
        exit_mode = self.skill_data.get("exit-mode", {})

        if exit_mode:
            self._add_result("Exit mode section", TestStatus.PASS,
                             "Exit mode procedures defined", category)
        else:
            self._add_result("Exit mode section", TestStatus.WARN,
                             "No explicit exit mode section", category)

    def test_metadata_discipline(self):
        """Test metadata discipline rules"""
        category = "Metadata Discipline"
        if "metadata-discipline" in self.skill_data:
            self._add_result("Metadata discipline", TestStatus.PASS,
                             "Metadata discipline rules defined", category)
        else:
            self._add_result("Metadata discipline", TestStatus.WARN,
                             "No metadata discipline section", category)

    def run_all_tests(self):
        """Run all test suites"""
        print("=" * 70)
        print("CHEEKY RAZOR SKILL.yaml TEST SUITE")
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
            self.test_metadata_discipline,
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
            "warnings": sum(1 for r in self.results if r.status == TestStatus.WARN),
        }

        print("=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print(f"Total Tests:  {summary['total']}")
        print(f"✓ Passed:     {summary['passed']}")
        print(f"✗ Failed:     {summary['failed']}")
        print(f"⚠ Warnings:   {summary['warnings']}")
        print()

        if summary["failed"] == 0:
            print("✓ ALL CRITICAL TESTS PASSED")
            success_rate = (summary["passed"] / summary["total"]) * 100
            print(f"  Success rate: {success_rate:.1f}%")
        else:
            print("✗ SOME TESTS FAILED - Review required")

        print("=" * 70)

        return summary


def main():
    """Main test runner"""
    tester = CheekyRazorSkillTester()
    summary = tester.run_all_tests()

    if summary["failed"] > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
