<?php
declare(strict_types=1);
function steps(int $number, int $steps = 0): int
{
    if ($number > 1) {
        if ($number % 2 == 0) {
            $number = $number/2;
            $steps += 1;
            return steps($number, $steps);
        } else {
            $number = ($number * 3) + 1;
            $steps += 1;
            return steps($number, $steps);
        }
    } elseif ($number == 1) {
        return $steps;
    } else {
        throw new InvalidArgumentException("Only positive numbers are allowed");
    }
}    
