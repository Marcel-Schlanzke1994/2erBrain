#pragma once
namespace gameplay { class HealthComponent{ public: explicit HealthComponent(int max); void damage(int amount); void heal(int amount); [[nodiscard]] int current() const; [[nodiscard]] bool alive() const; private: int max_; int current_; }; }
